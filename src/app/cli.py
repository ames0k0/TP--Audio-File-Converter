import os
import textwrap
import argparse

from afc import Converter


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Audio file converter",
        epilog=textwrap.dedent(
            """\
            Usage Example
                \r\tuv run python cli.py -i samples/BAK.wav -o samples/BAK.mp3
            """
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument("-i", "--input", help="Input audio filepath")
    parser.add_argument("-o", "--output", help="Output audio filepath")

    args = parser.parse_args()

    if not all((args.input, args.output)):
        parser.print_help()
        exit(1)
    
    converter = Converter()

    try:
        converter.set_input(filepath=args.input)
    except Exception as e:
        exit(e.args[0])

    output_filepath, output_fileext = os.path.splitext(args.output)

    try:
        converter.set_output(output_fileext[1:])
    except Exception as e:
        exit(e.args[0])

    converted_audio_file = converter.convert()

    with open(args.output, "wb") as ftwb:
        ftwb.write(converted_audio_file)
