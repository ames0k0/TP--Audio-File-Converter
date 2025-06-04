import io

import filetype
import pydub


class NonSequentialCallExp(Exception):
    pass
class UnsupportedFileTypeExp(Exception):
    pass
class UnsupportedExportFileFormatExp(Exception):
    pass


class Converter:
    """Audio file converter
    """

    SUPPORTED_FILE_TYPES: tuple[str] = (
        "audio/x-wav",
    )
    SUPPORTED_EXPORT_FILE_FORMAT: tuple[str] = (
        "mp3",
    )

    _filepath: str = ""
    _export_file_format: str = ""

    def set_input(self, filepath: str):
        self._filepath = filepath
        kind = filetype.guess(self._filepath)

        if not kind:
            raise UnsupportedFileTypeExp(
                "FileType is not supporeted, try:\n%s" % self.SUPPORTED_FILE_TYPES
            )
        if kind.mime not in self.SUPPORTED_FILE_TYPES:
            raise UnsupportedFileTypeExp(
                "FileType(`%s`) is not supporeted, try:\n%s" % (
                    kidn.mime, self.SUPPORTED_FILE_TYPES
                )
            )

    def set_output(self, export_file_format: str):
        if not self._filepath:
            raise NonSequentialCallExp("FilePath is not set, use: `set_input()`")

        self._export_file_format: str = str(export_file_format).lower()

        if self._export_file_format not in self.SUPPORTED_EXPORT_FILE_FORMAT:
            raise UnsupportedExportFileFormatExp(
                "FileFormat(`%s`) is not supported, use:\n%s" % (
                    self._export_file_format, self.SUPPORTED_EXPORT_FILE_FORMAT,
                )
            )

    def convert(self) -> bytes:
        """Returns converted `wav` to `mp3` as bytes"""
        if not self._filepath:
            raise NonSequentialCallExp("FilePath is not set, use: `set_input()`")
        if not self._export_file_format:
            raise NonSequentialCallExp("FilePath is not set, use: `set_output()`")

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
