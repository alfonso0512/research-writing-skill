#!/usr/bin/env python3
"""Title Case and Sentence case converter for academic figure/table captions.

Converts text between Title Case and Sentence case, preserving acronyms
and LaTeX math mode. Follows standard academic publishing conventions:
- Title Case: Capitalize first, last, and all major words.
- Sentence case: Capitalize first word and proper nouns only.

Usage:
    python title_case.py -i "performance comparison on imagenet" -s title
    python title_case.py -i caption.txt -o formatted.txt -s sentence
"""

import argparse
import re
import sys
from typing import Set


# Words that are NOT capitalized in Title Case (unless first or last)
MINOR_WORDS: Set[str] = {
    # Articles
    "a", "an", "the",
    # Coordinating conjunctions
    "and", "but", "or", "nor", "for", "so", "yet",
    # Short prepositions (3 letters or fewer)
    "at", "by", "in", "of", "on", "to", "up", "as",
    "is", "it", "be", "am", "are", "was", "were",
    "for", "from", "per", "via", "with",
}


def load_acronyms(filepath: str) -> Set[str]:
    """Load preserved acronyms from file (one per line)."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return {line.strip() for line in f if line.strip()}
    except FileNotFoundError:
        print(f"Warning: Acronym file not found: {filepath}", file=sys.stderr)
        return set()


def to_title_case(text: str, acronyms: Set[str]) -> str:
    """Convert text to Title Case.

    Preserves:
    - Acronyms and proper nouns (from acronyms set)
    - LaTeX math mode ($...$, $$...$$)
    - Hyphenated words: each part treated independently
    """
    # Split math segments
    result_parts = []
    last_end = 0
    for match in re.finditer(r"(\$\$[\s\S]*?\$\$|\$[^$]*?\$)", text):
        if match.start() > last_end:
            result_parts.append(
                _title_case_segment(
                    text[last_end : match.start()], acronyms
                )
            )
        result_parts.append(match.group(0))
        last_end = match.end()
    if last_end < len(text):
        result_parts.append(
            _title_case_segment(text[last_end:], acronyms)
        )

    return "".join(result_parts)


def _title_case_segment(text: str, acronyms: Set[str]) -> str:
    """Apply Title Case to a non-math segment."""
    words = text.split()
    if not words:
        return text

    result = []
    for i, word in enumerate(words):
        lower = word.lower()
        # Preserve known acronyms
        if word.upper() in acronyms or word in acronyms or _is_acronym(word):
            result.append(word.upper() if word.isupper() else word)
        # First and last words always capitalized
        elif i == 0 or i == len(words) - 1:
            result.append(_capitalize_word(word))
        # Minor words lowercase (unless they appear after colon/semicolon)
        elif lower in MINOR_WORDS:
            result.append(lower)
        # Hyphenated: capitalize each part
        elif "-" in word:
            parts = word.split("-")
            capped = "-".join(_capitalize_word(p) for p in parts)
            result.append(capped)
        else:
            result.append(_capitalize_word(word))

    return " ".join(result)


def to_sentence_case(text: str, acronyms: Set[str]) -> str:
    """Convert text to Sentence case.

    Only first word is capitalized. Preserves acronyms and math mode.
    """
    result_parts = []
    last_end = 0
    for match in re.finditer(r"(\$\$[\s\S]*?\$\$|\$[^$]*?\$)", text):
        if match.start() > last_end:
            result_parts.append(
                _sentence_case_segment(
                    text[last_end : match.start()], acronyms
                )
            )
        result_parts.append(match.group(0))
        last_end = match.end()
    if last_end < len(text):
        result_parts.append(
            _sentence_case_segment(text[last_end:], acronyms)
        )

    return "".join(result_parts)


def _sentence_case_segment(text: str, acronyms: Set[str]) -> str:
    """Apply Sentence case to a non-math segment."""
    if not text.strip():
        return text

    # Split into sentences
    sentences = re.split(r"(?<=[.!?])\s+", text)
    result = []
    for sent in sentences:
        words = sent.split()
        if not words:
            result.append(sent)
            continue

        capped = []
        for i, word in enumerate(words):
            if i == 0:
                capped.append(_capitalize_word(word))
            elif word.upper() in acronyms or _is_acronym(word):
                capped.append(word.upper() if word.isupper() else word)
            else:
                capped.append(word.lower())
        result.append(" ".join(capped))

    return " ".join(result)


def _capitalize_word(word: str) -> str:
    """Capitalize first letter of word, preserving rest."""
    if not word:
        return word
    return word[0].upper() + word[1:]


def _is_acronym(word: str) -> bool:
    """Check if a word looks like an acronym (all caps, 2+ letters)."""
    return bool(re.match(r"^[A-Z]{2,}$", word))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert text between Title Case and Sentence case.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Examples:\n"
        "  python title_case.py -i 'hello world' -s title\n"
        "  python title_case.py -i caption.txt -s sentence",
    )
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        help="Input text or file path (reads from stdin if omitted).",
    )
    parser.add_argument(
        "-s",
        "--style",
        choices=["title", "sentence"],
        default="title",
        help="Case style: title or sentence (default: title).",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Output file path (writes to stdout if omitted).",
    )
    parser.add_argument(
        "-a",
        "--preserve-acronyms",
        type=str,
        help="File with acronyms to preserve (one per line).",
    )

    args = parser.parse_args()

    # Read input
    if args.input:
        # Check if it's a file path or inline text
        try:
            with open(args.input, "r", encoding="utf-8") as f:
                text = f.read()
        except FileNotFoundError:
            text = args.input
    else:
        text = sys.stdin.read()

    # Load acronyms
    acronyms: Set[str] = set()
    if args.preserve_acronyms:
        acronyms = load_acronyms(args.preserve_acronyms)

    # Convert
    if args.style == "title":
        result = to_title_case(text, acronyms)
    else:
        result = to_sentence_case(text, acronyms)

    # Write output
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
    else:
        sys.stdout.write(result)


if __name__ == "__main__":
    main()
