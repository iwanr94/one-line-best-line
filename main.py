"""One Line, Best Line -- writes a single entertaining line to /output/entry.txt.

Stdlib only. No network, no third-party imports.
"""

from pathlib import Path

LINE = "My smart fridge emailed me about my midnight snacking, and I have never been judged so politely by an appliance."


def main() -> None:
    # Gate guard: the entry must be exactly one line, 1-240 chars, not blank.
    assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} chars, must be 1-240"
    assert "\n" not in LINE and LINE.strip(), "line must be a single non-blank line"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
