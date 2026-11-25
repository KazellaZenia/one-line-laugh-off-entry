"""One-Line Laugh-Off entry.

Writes exactly one funny line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure Python standard library; no third-party imports.
"""

import os
from pathlib import Path

# The twist lands on the last clause: the headphones work too well, and
# the only sound left to hear is the wearer themself.
LINE = "I bought noise-cancelling headphones to hear myself think; now all I hear is how loud I chew."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
