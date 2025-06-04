import pydub


def converter():
    audio_segment = pydub.AudioSegment.from_wav(
        "./samples/BAK.wav"
    )
    audio_segment.export(
        "./samples/BAK.mp3",
        format="mp3",
    )


if __name__ == "__main__":
    converter()
