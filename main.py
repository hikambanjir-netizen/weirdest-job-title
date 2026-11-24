#!/usr/bin/env python3
"""Weirdest Job Title entry.

Writes a single job title -- the weirdest one we could think of -- to
``entry.txt`` in the output directory, and nothing else. The blind judge
compares titles two at a time and picks the weirder, funnier one, so the
title is a real-sounding corporate job with one hilariously specific twist:
a senior title, an invented job, and a billionaire-yacht detail.

Pure standard library, deterministic, no network, no input files.
"""

import os
from pathlib import Path

TITLE = "Senior Apologizer for Billionaires' Yachts"


def main() -> None:
    # The sealed scorer accepts UTF-8 text of 1 to 60 characters, not only
    # whitespace. Enforce the contract here so an invalid title can never
    # reach the judge: one title, 42 characters, nothing else, no newline.
    text = TITLE.strip()
    if not 1 <= len(text) <= 60:
        raise ValueError(f"job title must be 1-60 characters, got {len(text)}")
    if text != TITLE or "\n" in text:
        raise ValueError("entry must be exactly the single job title")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # write_text with the bare string: no trailing newline is added.
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
