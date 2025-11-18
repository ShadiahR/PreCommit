# hooks/require_readme.py
import sys
from pathlib import Path


ACCEPTABLE_NAMES = {
    "README",
    "README.md",
    "readme.md",
    "Readme.md",
}


def repo_has_readme(repo_root: Path) -> bool:
    for name in ACCEPTABLE_NAMES:
        if (repo_root / name).exists():
            return True
    return False


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    repo_root = Path.cwd().resolve()

    if not repo_has_readme(repo_root):
        print("❌ Commit blocked: This repository must contain a README file.")
        print("Add one of the allowed names:")
        for name in ACCEPTABLE_NAMES:
            print(f"  - {name}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
