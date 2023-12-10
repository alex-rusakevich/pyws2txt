#!/usr/bin/env python3

import argparse
import os
from pathlib import Path

from serializer.txt import serialize as txt_serialize

ALLOWED_EXT = (
    "",
    ".doc",
    ".ws",
    ".wsd",
    ".ws6",
    ".ws7",
    ".ws4",
    ".ws3",
    ".ws2",
    ".ws1",
    ".ws5",
)


def is_ext_correct(filepath: str) -> bool:
    result = os.path.splitext(filepath)[1].lower() in ALLOWED_EXT
    result or print(f"Filtered file '{filepath}' out")

    return result


def main():
    # region Parsing args
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

    args = parser.parse_args()
    # endregion

    # region Populating working paths
    file_paths = []

    if os.path.isfile(args.work_path):
        file_paths.append(args.work_path)
    else:
        if args.recursive:
            file_paths = list(Path(args.work_path).rglob("*"))
        else:
            file_paths = list(Path(args.work_path).iterdir())

        file_paths = [f for f in file_paths if f.is_file()]

    if not args.no_ext_check:  # Filter paths by their extension
        file_paths = [f for f in file_paths if is_ext_correct(f)]
    # endregion

    if args.type == "txt":
        txt_serialize(file_paths, encoding=args.encoding)

    print("Done!")


if __name__ == "__main__":
    main()
