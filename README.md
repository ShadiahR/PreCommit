# Team Pre-commit Hooks (Python)

Reusable **pre-commit hooks** to keep code clean, consistent, and professional.

---

## Hooks Included

### 1. `block-long-comments`
Blocks **any comment block that is 3 or more consecutive lines**.

Short comments (1–2 lines) are allowed.

Useful for preventing:
- Large commented-out code blocks
- Temporary "disable entire function" code comments

---

### 2. `require-readme`
Ensures the repository **always contains a README**.

Allowed names:
- `README`
- `README.md`
- `readme.md`
- `Readme.md`

If a README is missing, all commits are blocked.

---

### 3. `check-whitespace`
Blocks commits containing:
- Trailing spaces
- More than one blank line at the end of a file

Helps keep diffs clean.

---

## Using These Hooks in Your Project

### 1. Install pre-commit

```bash
pip install pre-commit
```

### 2. Create .pre-commit-config.yaml Configuration File

```
repos:
  - repo: https://github.com/ShadiahR/PreCommit   # relative path to your hooks repo
    rev: v0.1.0                       # or a specific commit hash later
    hooks:
      - id: block-long-comments
      - id: require-readme
      - id: check-whitespace
```

### 3. Install git hooks
```
pre-commit install
```