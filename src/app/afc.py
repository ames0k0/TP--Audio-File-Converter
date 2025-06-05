import os
import io

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

    SUPPORTED_FILE_EXTENSIONS: tuple[str] = (
        ".wav",
    )
    SUPPORTED_EXPORT_FILE_FORMAT: tuple[str] = (
        "mp3",
    )

    _filepath: str = ""
    _export_file_format: str = ""

    def set_input(self, filepath: str):
        self._filepath = filepath
        file_ext = os.path.splitext(self._filepath)[1]

        if not file_ext:
            raise UnsupportedFileExtensionExp(
                "InputFileExtension is required, try:\n%s" % self.SUPPORTED_FILE_EXTENSIONS
            )
        if file_ext not in self.SUPPORTED_FILE_EXTENSIONS:
            raise UnsupportedFileExtensionExp(
                "InputFileExtension(`%s`) is not supporeted, try:\n%s" % (
                    file_ext, self.SUPPORTED_FILE_EXTENSIONS
                )
            )
        if not os.path.isfile(self._filepath):
            raise FileNotFoundError("InputFilePath is not valid: %s" % self._filepath)

    def set_output(self, export_file_format: str):
        if not self._filepath:
            raise NonSequentialFuncCallExp("InputFilePath is not set, use: `set_input()`")

        self._export_file_format: str = str(export_file_format).lower()

        if not self._export_file_format:
            raise UnsupportedExportFileFormatExp(
                "OutputExportFileFormat is required, try:\n%s" % self.SUPPORTED_EXPORT_FILE_FORMAT
            )
        if self._export_file_format not in self.SUPPORTED_EXPORT_FILE_FORMAT:
            raise UnsupportedExportFileFormatExp(
                "OutputExportFileFormat(`%s`) is not supported, try:\n%s" % (
                    self._export_file_format, self.SUPPORTED_EXPORT_FILE_FORMAT,
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
