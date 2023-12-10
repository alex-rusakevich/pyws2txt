#!/usr/bin/env python3

import os
from pathlib import Path
from typing import Iterable, Union

from pyws2txt.args import get_parsed_args
from pyws2txt.serializer import ALLOWED_EXT
from pyws2txt.serializer.txt import serialize as txt_serialize


def is_ext_correct(filepath: Union[str, Path]) -> bool:
    result = os.path.splitext(filepath)[1].lower() in ALLOWED_EXT
    if result:
        print(f"Filtered file '{filepath}' out")

    return result


def main():
    args = get_parsed_args()

    # region Populating working paths
    file_paths: Iterable[Path] = []

    if os.path.isfile(args.work_path):
        file_paths.append(args.work_path)
    else:
        if args.recursive:
            file_paths = list(Path(args.work_path).rglob("*"))
        else:
            file_paths = list(Path(args.work_path).iterdir())

        file_paths = [f for f in file_paths if f.is_file() == True]

    if not args.no_ext_check:  # Filter paths by their extension
        file_paths = [f for f in file_paths if is_ext_correct(f)]
    # endregion

    if args.type == "txt":
        txt_serialize(file_paths, encoding=args.encoding)

    print("Done!")


if __name__ == "__main__":
    main()
