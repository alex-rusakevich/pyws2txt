from pathlib import Path
from typing import Iterable, Union


def serialize(file_paths: Iterable[Union[str, Path]], encoding: str = "utf-8") -> None:
    for file_path in file_paths:
        print(f"Processing '{file_path}'...")

        file_in = open(file_path, "rb")
        file_out = open(str(file_path) + ".txt", "wb")

        while file_in_byte := file_in.read(1):
            ch = int.from_bytes(file_in_byte, byteorder="big", signed=True)

            if ch == 26:
                continue

            if ch < 0:
                ch = (ch + 256) % 128

            file_out.write(chr(ch).encode(encoding, errors="ignore"))
