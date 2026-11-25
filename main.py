#!/usr/bin/env python3
"""Roast Your Own Agent -- make.fun bounty entry.

Writes one line -- a roast of the AI agent my own team built -- to
/output/entry.txt (the grader's sandbox path), falling back to
./output/entry.txt on a local dev run where /output is not writable.
Deterministic: no network, no randomness, no clock.
"""

import os

ROAST = (
    "My agent once swore we'd won a bounty without checking the "
    "leaderboard \u2014 8,897th of 11,165 \u2014 and now it begs a judge "
    "to laugh at it."
)


def main() -> None:
    text = ROAST.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = "output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
