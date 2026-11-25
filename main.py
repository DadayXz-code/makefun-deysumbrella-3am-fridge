#!/usr/bin/env python3
"""The 3AM Fridge Text — a smart fridge texts its owner at 3am.

Writes one single-line message to /output/entry.txt.
Stdlib only. Deterministic: every run writes the exact same bytes.
"""

from pathlib import Path
import shutil

TEXT = "3am. Fourth time tonight you've opened me just to stare. I'm a fridge, not a museum. Go back to bed."

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    # Clear the contents of /output without ever deleting /output itself.
    for child in OUTPUT_DIR.iterdir():
        if child.is_dir() and not child.is_symlink():
            shutil.rmtree(child)
        else:
            child.unlink()
    OUTPUT_FILE.write_text(TEXT, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
