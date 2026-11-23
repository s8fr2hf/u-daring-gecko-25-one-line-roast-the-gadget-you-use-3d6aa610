#!/usr/bin/env python3
"""Write the one-line gadget roast to /output/entry.txt.

Reads the roast from entry.txt next to this script and copies it to
/output/entry.txt, creating the output directory if needed.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    out_dir = "/output"
    dst = os.path.join(out_dir, "entry.txt")

    # The competition requires a single line of 1-200 characters.
    with open(src, "r", encoding="utf-8") as f:
        line = f.read().strip()
    if not (1 <= len(line) <= 200):
        sys.exit("entry.txt must be 1-200 characters, got %d" % len(line))

    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    print("Wrote roast to " + dst)


if __name__ == "__main__":
    main()
