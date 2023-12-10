#!/usr/bin/env python3

import argparse
import os
from pathlib import Path

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

    for file_path in file_paths:
        print(f"Processing '{file_path}'...")

        file_in = open(file_path, "rb")
        file_out = open(str(file_path) + ".txt", "w", encoding="utf8")

        while file_in_byte := file_in.read(1):
            ch = int.from_bytes(file_in_byte, signed=True)

            if ch == 26:
                continue

            if ch < 0:
                ch = (ch + 256) % 128

            file_out.write(chr(ch))

    print("Done!")


if __name__ == "__main__":
    main()
