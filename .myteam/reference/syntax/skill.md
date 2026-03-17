---
name: markdowndata-syntax
description: Complete syntax reference for all markdowndata value types
---

# markdowndata Syntax Reference

Every value in a markdowndata file is the content beneath a header. The content type is auto-detected.

---

## 1. YAML Dictionary (with header)

A YAML block delimited by `===` on its own lines.

**Markdown:**

```markdown
# settings

===
host: localhost
port: 5432
debug: false
===
```

**Python output:**

```python
{"settings": {"host": "localhost", "port": 5432, "debug": False}}
```

Notes:

- Standard YAML syntax inside `===` delimiters
- Keys become dict keys; values are typed by YAML rules
- `YYYY-MM-DD` date strings become `datetime.date` objects (use quotes to keep as string: `"2024-01-01"`)

---

## 2. MD Table (with header)

A Markdown table that is the **only** content under a header (no other text).

**Markdown:**

```markdown
# scores

| subject | grade |
|---------|-------|
| math    | 95    |
| english | 88    |
```

**Python output:**

```python
{"scores": [{"subject": "math", "grade": 95}, {"subject": "english", "grade": 88}]}
```

Notes:

- Returns a list of dicts — one dict per row, using column headers as keys
- Cell values are auto-converted: integers stay int, decimals become float, rest stay str
- If there is any other text in the section alongside the table, it falls back to MD text

---

## 3. MD List (with header)

A Markdown unordered list (`-` or `*`) that is the **only** content under a header.

**Markdown:**

```markdown
# tags

- python
- config
- markdown
```

**Python output:**

```python
{"tags": ["python", "config", "markdown"]}
```

Notes:

- Returns a plain list of values
- Values are auto-converted (integers, floats, strings)
- If there is any other text alongside the list, it falls back to MD text

---

## 4. MD Text (with header)

Any content that isn't purely YAML, a table, or a list — including prose, mixed content, inline code, and code blocks.

**Markdown:**

```markdown
# description

This is a **bold** description with `inline code`.

It can span multiple paragraphs.
```

**Python output:**

```python
{"description": "This is a **bold** description with `inline code`.\n\nIt can span multiple paragraphs."}
```

Notes:

- Returns a string; Markdown formatting is preserved as-is
- Soft line breaks (single newline) are joined with a space
- Paragraph breaks (double newline) are preserved
- Fenced code blocks are preserved exactly

---

## 5. Headless YAML Dictionary

A YAML block with `===` delimiters as the **entire file content** (no headers).

**Markdown:**

```markdown
===
name: Alice
age: 30
===
```

**Python output:**

```python
{"name": "Alice", "age": 30}
```

Notes:

- The file must contain only the YAML block — no headers, no other content
- Returns the dict directly (not nested under a key)

---

## 6. Headless MD Table

A Markdown table as the **entire file content** (no headers).

**Markdown:**

```markdown
| name  | score |
|-------|-------|
| Alice | 95    |
| Bob   | 88    |
```

**Python output:**

```python
[{"name": "Alice", "score": 95}, {"name": "Bob", "score": 88}]
```

Notes:

- Returns a list of dicts directly

---

## 7. Headless MD List

A Markdown list as the **entire file content** (no headers).

**Markdown:**

```markdown
- apple
- banana
- cherry
```

**Python output:**

```python
["apple", "banana", "cherry"]
```

---

## 8. Headless MD Text

Plain text or mixed Markdown as the **entire file content** (no headers).

**Markdown:**

```markdown
This is a plain text config value.
It can span multiple lines.
```

**Python output:**

```python
"This is a plain text config value. It can span multiple lines."
```

---

## Header Hierarchy and Nesting

Headers create nested dictionaries. `##` under `#` becomes a nested key:

```markdown
# database

## host

localhost

## port

5432
```

Output: `{"database": {"host": "localhost", "port": 5432}}`

When a section has **both** direct content and sub-headers, the direct content is stored under the key `"content"`:

```markdown
# settings

===
debug: false
===

## timeout

30
```

Output: `{"settings": {"content": {"debug": False}, "timeout": 30}}`

---

## Code Block Protection

Headers inside fenced code blocks are **not** parsed as section headers:

```markdown
# example

```markdown
# this header is ignored
```

Content here belongs to "example".

```

The `# this header is ignored` line is treated as literal text, not a new key.

---

## Type Conversion Rules

Values in tables, lists, and YAML are auto-converted:

| Input | Python type | Example |
|-------|-------------|---------|
| All digits | `int` | `"42"` → `42` |
| Contains `.` | `float` | `"3.14"` → `3.14` |
| YAML `YYYY-MM-DD` | `datetime.date` | `2024-01-01` → `date(2024, 1, 1)` |
| Quoted YAML date | `str` | `"2024-01-01"` → `"2024-01-01"` |
| Anything else | `str` | `"hello"` → `"hello"` |

YAML booleans (`true`/`false`) follow standard YAML rules → Python `True`/`False`.
