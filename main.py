#!/usr/bin/env python3
"""Writes the one-line houseplant review for the make.fun bounty."""

import os

REVIEW = (
    "★☆☆☆☆ My roots have circled this cracked pot so long they've formed a union, "
    "and he put a plastic fern next to me 'for company' — the fake one gets watered more than I do."
)


def main() -> None:
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = "output"
        os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
