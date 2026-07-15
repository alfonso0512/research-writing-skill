#!/usr/bin/env python3
"""LaTeX special character escaper for academic text.

Escapes common LaTeX special characters in plain text to prevent
compilation errors. Optionally preserves content inside math mode ($...$
and $$...$$).

Usage:
    python escape_latex.py -i input.txt -o output.txt
    python escape_latex.py -i input.txt --preserve-math
    echo "Test 50% complete" | python escape_latex.py
"""

import argparse
import re
import sys
from typing import List, Tuple


def escape_latex(
    text: str, preserve_math: bool = True
) -> str:
    """Escape LaTeX special characters in text.

    Args:
        text: Input text to escape.
        preserve_math: If True, preserve content inside $...$ and $$...$$.

    Returns:
        Escaped text.
    """
    if preserve_math:
        # Split into math and non-math segments
        segments: List[Tuple[str, bool]] = []
        pattern = re.compile(r"(\$\$[\s\S]*?\$\$|\$[^$]*?\$)")
        last_end = 0
        for match in pattern.finditer(text):
            if match.start() > last_end:
                segments.append((text[last_end : match.start()], False))
            segments.append((match.group(0), True))
            last_end = match.end()
        if last_end < len(text):
            segments.append((text[last_end:], False))

        escaped_segments = []
        for segment, is_math in segments:
            if is_math:
                escaped_segments.append(segment)
            else:
                escaped_segments.append(_do_escape(segment))
        return "".join(escaped_segments)
    else:
        return _do_escape(text)


def _do_escape(text: str) -> str:
    """Apply LaTeX escapes, skipping already-escaped characters."""
    # Order matters: escape \ first to avoid double-escaping,
    # but skip already-escaped patterns
    replacements = [
        # Backslash first (only for literal backslashes, not already escaped)
        # We handle this by only escaping backslashes NOT followed by known commands
        ("\\", r"\textbackslash{}"),
        ("{", r"\{"),
        ("}", r"\}"),
        ("#", r"\#"),
        ("$", r"\$"),
        ("%", r"\%"),
        ("&", r"\&"),
        ("~", r"\textasciitilde{}"),
        ("_", r"\_"),
        ("^", r"\^{}"),
    ]

    result = text
    for char, replacement in replacements:
        if char == "\\":
            # Only replace literal backslashes (not already part of commands)
            result = re.sub(
                r"(?<!\\)\\(?![" r"\\" r"#%&{}_~^$])",
                replacement,
                result,
            )
        else:
            # Skip if already preceded by backslash (already escaped)
            result = re.sub(
                rf"(?<!\\)[{re.escape(char)}]",
                replacement,
                result,
            )

    # Fix up the backslash case: \textbackslash{} was already handled above
    # Restore double-backslash (line breaks)
    result = result.replace(r"\textbackslash{}\textbackslash{}", r"\\")

    return result


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Escape LaTeX special characters in text.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Examples:\n"
        "  python escape_latex.py -i draft.txt -o escaped.txt\n"
        "  echo '50% complete' | python escape_latex.py",
    )
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        help="Input file path (reads from stdin if omitted).",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Output file path (writes to stdout if omitted).",
    )
    parser.add_argument(
        "-m",
        "--preserve-math",
        action="store_true",
        default=True,
        help="Preserve content inside $...$ and $$...$$ (default: True).",
    )
    parser.add_argument(
        "--no-preserve-math",
        action="store_false",
        dest="preserve_math",
        help="Escape everything including math mode content.",
    )
    parser.add_argument(
        "-n",
        "--dry-run",
        action="store_true",
        help="Show changes without writing output.",
    )

    args = parser.parse_args()

    # Read input
    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    # Escape
    escaped = escape_latex(text, preserve_math=args.preserve_math)

    if args.dry_run:
        if text == escaped:
            print("No changes needed.", file=sys.stderr)
        else:
            print(
                f"Would change {len(text)} chars → {len(escaped)} chars.",
                file=sys.stderr,
            )
        sys.exit(0)

    # Write output
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(escaped)
    else:
        sys.stdout.write(escaped)


if __name__ == "__main__":
    main()
