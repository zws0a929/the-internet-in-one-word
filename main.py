#!/usr/bin/env python3
"""The Internet in One Word — entry program.

Writes exactly one word to /output/entry.txt: "abyss".

Why this word: the whole internet, in one beat, is an abyss — an
endless void that holds everything at once. It is funny on its own,
true of the internet as a whole rather than one app or one mood, and
surprising: it is not the first obvious word anyone reaches for.
"""

import argparse
import sys
from pathlib import Path

# The single word that describes the whole internet.
#
# Why "abyss" beats the other candidates:
#   - "doomscroll" names one thing people DO on the internet, not the
#     internet itself, and it is already a household word — no surprise.
#   - "brainrot" names an effect of the content, a mood, not the whole
#     internet; it is also a familiar piece of slang by now.
#   - "abyss" names the whole thing at once: an endless void holding
#     everything. Five letters, instantly readable, lands in one beat,
#     funny on its own, and surprising — nobody's first guess.
ENTRY_WORD = "abyss"

# Gate limits from the competition rules: /output/entry.txt must be
# UTF-8 text of 1 to 30 characters, not only whitespace.
MIN_LENGTH = 1
MAX_LENGTH = 30

DEFAULT_OUTPUT = Path("/output/entry.txt")


def validate_word(word: str) -> str:
    """Check the entry word against the gate; fail loudly if invalid."""
    if not isinstance(word, str):
        raise TypeError("entry word must be a string")
    if not word.strip():
        raise ValueError("entry word must not be only whitespace")
    if word != word.strip():
        raise ValueError("entry word must not have leading/trailing whitespace")
    if len(word.split()) != 1:
        # A single word splits into exactly one token.
        raise ValueError("entry word must be a single word, no spaces")
    if not (MIN_LENGTH <= len(word) <= MAX_LENGTH):
        raise ValueError(
            f"entry word must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(word)}"
        )
    if not word.isprintable():
        raise ValueError("entry word must contain only printable characters")
    if not word.isalpha():
        # The word is a plain English word: letters only, no digits,
        # punctuation or symbols, so it lands in one beat.
        raise ValueError("entry word must contain only letters")
    return word


def write_entry(output_path: Path, word: str) -> None:
    """Write the word (and nothing else) to the output file as UTF-8.

    Deterministic: the same word, the same bytes, every run. No
    trailing newline, no extra whitespace — the file holds exactly
    the entry word, so its byte count equals the word's length.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(word.encode("utf-8"))


def verify_entry(output_path: Path, word: str) -> bool:
    """Re-read the file and confirm it holds exactly the word.

    Checks the raw bytes (no hidden newline or whitespace), the
    decoded text, and the gate rules, so a silent write error or a
    stray character cannot slip through unnoticed.
    """
    raw = output_path.read_bytes()
    if raw != word.encode("utf-8"):
        return False
    actual = raw.decode("utf-8")
    if actual != word:
        return False
    try:
        validate_word(actual)
    except (TypeError, ValueError):
        return False
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Write the one-word internet entry to /output/entry.txt."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="where to write entry.txt (default: /output/entry.txt)",
    )
    parser.add_argument(
        "--verify-only",
        action="store_true",
        help="only verify an existing entry.txt, do not write",
    )
    args = parser.parse_args(argv)

    word = validate_word(ENTRY_WORD)

    if args.verify_only:
        if not args.output.exists():
            print(f"error: {args.output} does not exist", file=sys.stderr)
            return 1
        if verify_entry(args.output, word):
            print(f"verified: {args.output} contains exactly {word!r}")
            return 0
        print(
            f"error: {args.output} does not contain exactly {word!r}",
            file=sys.stderr,
        )
        return 1

    write_entry(args.output, word)
    if not verify_entry(args.output, word):
        print(f"error: verification failed after writing {args.output}",
              file=sys.stderr)
        return 1
    size = args.output.stat().st_size
    print(f"wrote {word!r} ({size} bytes) to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
