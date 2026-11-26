#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line funny safety warning label for every human being
to /output/entry.txt. Fully deterministic: no network, no randomness,
no time, no input. One fixed string, written verbatim.
"""

import os

ENTRY = (
    "WARNING: This human is 70% water, 20% caffeine, and 10% feelings "
    "it refuses to discuss. Do not shake. May cry at dog food commercials."
)

DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"


def resolve_output_path() -> str:
    """Return the entry file path, honouring the grader's output dir."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    return os.path.join(out_dir, ENTRY_FILENAME)


def main() -> None:
    output_path = resolve_output_path()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
