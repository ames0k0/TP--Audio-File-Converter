import pytest

from main import Converter


class TestClass:

    @pytest.mark.parametrize(
        ("filepath",),
        (
            ("samples/BAK.wav",),
        )
    )
    def test_input(self, filepath: str):
        x = "this"
        assert "h" in x

    @pytest.mark.parametrize(
        ("export_file_format",),
        (
            ("mp3",),
        )
    )
    def test_ouput(self, export_file_format: str):
        x = "this"
        assert "h" in x

    @pytest.mark.parametrize(
        ("filepath", "export_file_format"),
        (
            ("samples/BAK.wav", "mp3"),
        )
    )
    def test_convert(self, filepath: str, export_file_format: str):
        x = "this"
        assert "h" in x
