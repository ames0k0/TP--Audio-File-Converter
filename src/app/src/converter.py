import os
import io
from typing import Sequence

import pydub


class NonSequentialFuncCallExp(Exception):
    pass
class UnsupportedFileExtensionExp(Exception):
    pass
class UnsupportedExportFileFormatExp(Exception):
    pass


class Converter:
    """Audio file converter
    """

    SUPPORTED_FILE_EXTENSIONS: Sequence[str] = (
        ".wav",
    )
    SUPPORTED_EXPORT_FILE_FORMATS: Sequence[str] = (
        "mp3",
    )
    MAP_FILE_FORMAT_TO_FILE_MIMETYPE: dict[str, str] = {
        "mp3": "audio/mpeg",
    }

    _filepath: str = ""
    _export_file_format: str = ""

    def _join_sequence(self, items: Sequence[str]) -> str:
        return ", ".join(items)

    def set_input(self, filepath: str):
        self._filepath = filepath
        file_ext = os.path.splitext(self._filepath)[1]

        if not file_ext:
            raise UnsupportedFileExtensionExp(
                "InputFileExtension is required, try: %s" % self._join_sequence(
                    self.SUPPORTED_FILE_EXTENSIONS
                )
            )
        if file_ext not in self.SUPPORTED_FILE_EXTENSIONS:
            raise UnsupportedFileExtensionExp(
                "InputFileExtension: `%s` is not supporeted, try: %s" % (
                    file_ext,
                    self._join_sequence(self.SUPPORTED_FILE_EXTENSIONS),
                )
            )
        if not os.path.isfile(self._filepath):
            raise FileNotFoundError("InputFilePath is not valid: %s" % self._filepath)

    def set_output(self, export_file_format: str):
        self._export_file_format: str = str(export_file_format).lower()

        if not self._export_file_format:
            raise UnsupportedExportFileFormatExp(
                "OutputExportFileFormat is required, try: %s" % self._join_sequence(
                    self.SUPPORTED_EXPORT_FILE_FORMATS
                )
            )
        if self._export_file_format not in self.SUPPORTED_EXPORT_FILE_FORMATS:
            raise UnsupportedExportFileFormatExp(
                "OutputExportFileFormat: `%s` is not supported, try: %s" % (
                    self._export_file_format,
                    self._join_sequence(
                        self.SUPPORTED_EXPORT_FILE_FORMATS
                    ),
                )
            )

    def convert(self) -> bytes:
        """Returns converted `wav` to `mp3` as bytes"""
        if not self._filepath:
            raise NonSequentialFuncCallExp("InputFilePath is not set, use: `set_input()`")
        if not self._export_file_format:
            raise NonSequentialFuncCallExp("OuputExportFileFormat is not set, use: `set_output()`")

        audio_export = io.BytesIO()

        audio_segment = pydub.AudioSegment.from_wav(
            file=self._filepath
        )
        audio_segment.export(audio_export, format=self._export_file_format)

        return audio_export.getvalue()


if __name__ == "__main__":
    converter = Converter()

    converter.set_input(filepath="./samples/BAK.wav")
    converter.set_output(export_file_format="mp3")

    converted_audio_file = converter.convert()

    with open("./samples/BAK.mp3", "wb") as ftwb:
        ftwb.write(converted_audio_file)
