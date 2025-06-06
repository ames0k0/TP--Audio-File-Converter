import os
from typing import Sequence
from tempfile import NamedTemporaryFile

from django.urls import path
from django.http import FileResponse
from django.forms import fields
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import response, serializers
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.exceptions import APIException

from converter import Converter


class AudioConverterGetOut(serializers.Serializer):
    SUPPORTED_FILE_EXTENSIONS: Sequence[str] = serializers.ListField(
        child=serializers.CharField(),
    )
    SUPPORTED_EXPORT_FILE_FORMATS: Sequence[str] = serializers.ListField(
        child=serializers.CharField(),
    )


class MissingAudioFileExp(APIException):
    status_code=400
    default_detail="Audio `file` is required."
    default_code="missing_input_file"


class MissingQueryParamExp(APIException):
    status_code=400
    default_detail="Query param `export_file_format` is required."
    default_code="missing_input_query_param"


class ConverterErrorExp(APIException):
    status_code=400
    default_code="converter_error"
    def __init__(self, detail):
        super().__init__()
        self.detail=detail


class AudioConverterView(APIView):
    allowed_methods: list[str] = ["GET", "POST"]
    parser_classes: list = [MultiPartParser]

    def get(self, request):
        """Get audio converter meta"""
        serializer = AudioConverterGetOut({
            "SUPPORTED_FILE_EXTENSIONS": Converter.SUPPORTED_FILE_EXTENSIONS,
            "SUPPORTED_EXPORT_FILE_FORMATS": Converter.SUPPORTED_EXPORT_FILE_FORMATS,
        })
        return response.Response(serializer.data)

    def post(self, request):
        file = request.data.get("file")
        if not file:
            raise MissingAudioFileExp()

        export_file_format = request.query_params.get("export_file_format")
        if not export_file_format:
            raise MissingQueryParamExp()

        converted_audio_file: bytes | None = None

        converter = Converter()
        filename, fileext = os.path.splitext(file.name)

        with NamedTemporaryFile(suffix=fileext, mode="wb", delete=False) as ftwb:
            ftwb.write(file.read())

        try:
            converter.set_input(filepath=ftwb.name)
            converter.set_output(export_file_format=export_file_format)

            converted_audio_file = converter.convert()
        except Exception as e:
            raise ConverterErrorExp(detail=e.args[0])
        finally:
            os.remove(ftwb.name)

        return FileResponse(
            converted_audio_file,
            as_attachment=True,
            filename=f"{filename}.{export_file_format}",
        )


urlpatterns = staticfiles_urlpatterns() + [
    path("", AudioConverterView.as_view()),
]
