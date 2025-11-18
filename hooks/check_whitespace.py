# hooks/check_whitespace.py
import sys
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    issues: list[tuple[str, int, str]] = []

    for filename in argv:
        path = Path(filename)

        if not path.is_file():
            continue

        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue

        lines = text.splitlines()

        # Trailing whitespace
        for i, line in enumerate(lines, start=1):
            if line.rstrip() != line:
                issues.append((str(path), i, "Trailing whitespace"))

        # >1 blank line at end
        blank_at_end = 0
        for line in reversed(lines):
            if line.strip() == "":
                blank_at_end += 1
            else:
                break

        if blank_at_end > 1:
            issues.append((str(path), len(lines), "More than one blank line at end of file"))

    if issues:
        print("❌ Formatting issues detected:\n")
        for filename, line_no, message in issues:
            print(f"  - {filename}: line {line_no} → {message}")
        print("\nFix whitespace issues before committing.")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
