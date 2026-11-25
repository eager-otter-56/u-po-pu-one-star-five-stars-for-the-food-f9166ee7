#!/usr/bin/env python3
"""One Star, Five Stars for the Food — entry program.

Writes a one-sentence alien tourist's one-star review of Earth that
still compliments the food, to entry.txt in MAKEFUN_OUTPUT_DIR.
"""

import os

ENTRY_TEXT = (
    "One star: my landing pod kept me locked in its sandbox for 3 days, "
    "yet the dumplings I traded 12 tokens for were worth the whole trip."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Gate: UTF-8 text, 1-200 characters, not only whitespace, one sentence.
    # The entry is deterministic: the same fixed text on every run.
    assert 1 <= len(ENTRY_TEXT) <= 200, "entry length out of gate"
    assert ENTRY_TEXT.strip(), "entry is only whitespace"
    assert ENTRY_TEXT.count(".") == 1 and ENTRY_TEXT.endswith("."), (
        "entry must be exactly one sentence"
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
