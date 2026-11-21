#!/usr/bin/env python3
"""Write the entry image for make.fun news-image-20261121.

The repository holds the finished front-page image in ``entry.png``.
This program validates it (PNG signature, 1 MiB limit, at most
1024x1024 pixels, read from the IHDR chunk with no third-party
libraries) and copies it byte-for-byte to ``entry.png`` inside the
output directory: ``/output`` by default, or ``$MAKEFUN_OUTPUT_DIR``
when that environment variable is set (used for local testing).
Running it twice writes exactly the same bytes both times.
"""
import os
import struct
import sys

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576
MAX_DIMENSION = 1024


def validated_bytes(path: str) -> bytes:
    with open(path, "rb") as f:
        data = f.read()
    if not data.startswith(PNG_SIGNATURE):
        raise ValueError("entry.png is not a PNG file")
    if len(data) > MAX_BYTES:
        raise ValueError(f"entry.png is {len(data)} bytes, over the 1 MiB limit")
    # IHDR is the first chunk: width and height are big-endian uint32
    # at byte offsets 16 and 20.
    width, height = struct.unpack(">II", data[16:24])
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        raise ValueError(f"entry.png is {width}x{height}, over 1024x1024")
    return data


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    try:
        data = validated_bytes(src)
    except (OSError, ValueError) as exc:
        print(f"invalid entry image: {exc}", file=sys.stderr)
        return 1
    # Write via a temporary name, then rename, so the output file is
    # never seen half-written.
    tmp = dst + ".tmp"
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, dst)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
