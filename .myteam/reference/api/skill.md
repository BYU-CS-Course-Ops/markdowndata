---
name: markdowndata-api
description: Python API reference for markdowndata — loads() and load() functions
---

# markdowndata Python API

## Import

```python
import markdowndata
```

---

## `markdowndata.loads(text: str) -> dict | list | str`

Parse a Markdown string into structured Python data.

**Parameters:**

- `text` — a string containing Markdown content

**Returns:** `dict`, `list`, or `str` depending on the content structure

**Example:**

```python
import markdowndata

text = """
# name

Alice

# age

30
"""

data = markdowndata.loads(text)
# {"name": "Alice", "age": 30}
```

---

## `markdowndata.load(file) -> dict | list | str`

Parse a Markdown file object into structured Python data.

**Parameters:**

- `file` — any file-like object with a `.read()` method

**Returns:** same as `loads()`

**Example:**

```python
import markdowndata

with open("config.md") as f:
    data = markdowndata.load(f)
```

---

## Common access patterns

```python
import markdowndata

with open("config.md") as f:
    data = markdowndata.load(f)

# Simple key access
name = data["name"]

# Nested key access
host = data["database"]["host"]

# List access
first_tag = data["tags"][0]

# Table row access
first_score = data["scores"][0]["grade"]

# YAML dict access
version = data["metadata"]["version"]
```

---

## Headless files

If the `.md` file has no headers (headless), the return value is the parsed content directly:

```python
# headless list file:  "- a\n- b\n- c"
data = markdowndata.loads("- a\n- b\n- c")
# ["a", "b", "c"]  — a list, not a dict

# headless YAML file
data = markdowndata.loads("===\nfoo: bar\n===")
# {"foo": "bar"}
```

---

## Error conditions

- **Empty content** — `loads("")` returns `{}` (empty dict)
- **Content that cannot be parsed** — raises `ValueError` with a description
- **Malformed YAML inside `===` block** — raises a YAML parse error from the `yaml` library
- **File not found** — raises `FileNotFoundError` from standard `open()`; `markdowndata.load()` does not open files
  itself

---

## Notes

- `load(file)` calls `file.read()` and passes the result to `loads()` — it does not accept a file path string
- To load from a path string, use `open()`:
  ```python
  with open(path) as f:
      data = markdowndata.load(f)
  ```
- Both functions are stateless — create a new call for each parse; no shared state between calls
