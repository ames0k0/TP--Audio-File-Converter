import pytest

from afc import (
    NonSequentialFuncCallExp,
    UnsupportedFileExtensionExp,
    UnsupportedExportFileFormatExp
)
from afc import Converter


class TestConverter:

    @pytest.mark.parametrize(
        ("filepath", "exception"),
        (
            ("samples/WrongFilePath.wav", FileNotFoundError),
            ("samples/BAK.mp3", UnsupportedFileExtensionExp),
        )
    )
    def test_input(
        self,
        filepath: str,
        exception: Exception
    ):
        """Checks for file path and type

        Supported file types are:
            `SUPPORTED_FILE_TYPES`
        """
        converter = Converter()

        with pytest.raises(exception):
            converter.set_input(filepath=filepath)

    @pytest.mark.parametrize(
        ("filepath", "export_file_format", "exception"),
        (
            ("samples/BAK.wav", "mp3", NonSequentialFuncCallExp),
            ("samples/BAK.wav", "wav", UnsupportedExportFileFormatExp),
        )
    )
    def test_ouput(
        self,
        filepath: str,
        export_file_format: str,
        exception: Exception
    ):
        """Checks for export file format

        Supported export file formats are:
            `SUPPORTED_EXPORT_FILE_FORMATS`
        """
        converter = Converter()

        if exception is not NonSequentialFuncCallExp:
            converter.set_input(filepath=filepath)

        with pytest.raises(exception):
            converter.set_output(export_file_format=export_file_format)

    @pytest.mark.parametrize(
        ("filepath", "export_file_format", "exception", "task_id"),
        (
            ("samples/BAK.wav", "mp3", NonSequentialFuncCallExp, 1),
            ("samples/BAK.wav", "mp3", NonSequentialFuncCallExp, 2),
        )
    )
    def test_convert(
        self,
        filepath: str,
        export_file_format: str,
        exception: Exception,
        task_id: int
    ):
        """Checks for sequential function call

        Correct SFC order:
            `set_input()`
            `set_output()`
            `convert()`
        """
        converter = Converter()

        if task_id != 1:
            converter.set_input(filepath=filepath)

        with pytest.raises(exception):
            converter.convert()
