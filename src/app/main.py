import io

import pydub


class Converter:
    """Audio file converter
    """
    _filepath: str = ""
    _export_file_format: str = ""

    def set_input(self, filepath: str):
        self._filepath = filepath

    def set_output(self, export_file_format: str = "mp3"):
        self._export_file_format = export_file_format

    def convert(self) -> bytes:
        """Returns converted `wav` to `mp3` as bytes"""
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

    with open("./samples/BAK.mp3", "wb") as ftwb:
        ftwb.write(converter.convert())
