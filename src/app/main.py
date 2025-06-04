import io

import pydub


def converter(filepath: str) -> bytes:
    audio_export = io.BytesIO()

    audio_segment = pydub.AudioSegment.from_wav(file=filepath)
    audio_segment.export(audio_export, format="mp3")

    return audio_export.getvalue()


if __name__ == "__main__":
    output: bytes = converter(filepath="./samples/BAK.wav")

    with open("./samples/BAK.mp3", "wb") as ftwb:
        ftwb.write(output)
