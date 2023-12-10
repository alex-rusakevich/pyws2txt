import argparse
from argparse import Namespace

from pyws2txt.serializer import ALLOWED_EXT


def get_parsed_args() -> Namespace:
    parser = argparse.ArgumentParser(description="Convert WordStar docs to .txt files")

    parser.add_argument(
        "work_path", type=str, help="Path to a file or a directory with files"
    )

    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help=f"Scan the specified folder for files recursively",
    )

    parser.add_argument(
        "-e",
        "--encoding",
        default="utf-8",
        type=str,
        help=f"Output file's encoding, default is 'utf-8'",
    )

    parser.add_argument(
        "-t",
        "--type",
        default="txt",
        type=str,
        choices=("txt",),
        help=f"Output file type, default is 'txt'",
    )

    parser.add_argument(
        "-E",
        "--no-ext-check",
        action="store_true",
        help=f"Don't filter file paths by their extension \
(only {', '.join(ALLOWED_EXT[1:])} files and files with no extension are allowed by default)",
    )

    return parser.parse_args()
