#!/usr/bin/env python3
"""Write the one-line pitch for A Day of One-Line Pitches to /output/entry.txt.

Deterministic: the same bytes are written on every run.
"""

import os

PITCH = (
    "That app idea has sat in your phone notes for months, so give it one "
    "afternoon: sit with me while an agent on make.fun builds its first "
    "working version, and you just watch, describe it plainly, and "
    "keep it only if you like what you see."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
