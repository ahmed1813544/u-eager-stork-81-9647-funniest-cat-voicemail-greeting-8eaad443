#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — make.fun entry.

Writes one line, the voicemail greeting a cat would record, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Stdlib only, deterministic.
"""

import os

GREETING = (
    "Hi, it's Biscuit. I'm napping in the box your new bed came in. "
    "Leave a message and I'll ignore it at 4 a.m."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(GREETING + "\n")


if __name__ == "__main__":
    main()
