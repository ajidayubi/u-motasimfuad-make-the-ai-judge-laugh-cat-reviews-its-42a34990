#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one single-line one-star review, written in the voice of a house
cat about its human, to /output/entry.txt. The review is a fixed,
deterministic string: no network, no input files, no randomness, no
model calls. The program validates the review against the competition
gate (UTF-8 text, 1 to 200 characters, a single line, not only white
space) before and after writing it.
"""

import os
import sys

# The review: the cat files a performance review of its own. The human
# is judged by cat standards (a caught mouse is a deliverable), and the
# sting lands in the last few words, when the cat concludes that
# management -- the human -- cannot take honest feedback.
REVIEW = (
    "One star. I brought him a mouse as a performance review and he "
    "screamed, so clearly management is not ready for honest feedback."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the review against the competition gate."""
    if not isinstance(text, str):
        raise ValueError("review is not text")
    if not text.strip():
        raise ValueError("review is only white space")
    if len(text) < 1 or len(text) > 200:
        raise ValueError("review must be 1 to 200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    for ch in text:
        if ord(ch) < 0x20 and ch not in ("\t",):
            raise ValueError("review holds a control character")
    text.encode("utf-8")  # must be valid UTF-8 text


def main():
    validate(REVIEW)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(REVIEW + "\n")
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != REVIEW + "\n":
        raise ValueError("written entry does not match the review")
    validate(written.rstrip("\n"))
    print(REVIEW)
    print("chars: %d" % len(REVIEW), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
