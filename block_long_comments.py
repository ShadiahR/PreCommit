# hooks/block_long_comments.py
import sys
from pathlib import Path

EXCEPTION_PREFIXES = (
    "#!",
    "# -*- coding:",
)


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    offending_files = []

    for filename in argv:
        path = Path(filename)

        if not path.is_file() or path.suffix != ".py":
            continue

        try:
            lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        except OSError:
            continue

        in_comment_block = 0

        for line in lines:
            stripped = line.strip()

            # Skip empty lines
            if stripped == "":
                in_comment_block = 0
                continue

            # Skip special exception comment lines
            if any(stripped.startswith(prefix) for prefix in EXCEPTION_PREFIXES):
                continue

            # If line starts with "#", count it
            if stripped.startswith("#"):
                in_comment_block += 1
            else:
                # reset counter when normal code appears
                in_comment_block = 0

            # If we hit 3 consecutive commented lines -> block
            if in_comment_block >= 3:
                offending_files.append(path)
                break

    if offending_files:
        print("❌ Commit blocked: Long comment blocks (3+ lines) detected.")
        print("These files contain long commented-out code:")
        for f in offending_files:
            print(f"  - {f}")
        print("\nShort comments (1–2 lines) are allowed.")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
