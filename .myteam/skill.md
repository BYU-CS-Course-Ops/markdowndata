---
name: markdowndata
description: Use markdowndata to create or edit .md config files as structured Python data
---

# markdowndata

`markdowndata` is a Python library that parses Markdown files into structured Python dictionaries. It lets you use plain
`.md` files as human-readable configuration — a lightweight alternative to YAML/JSON that is readable as documentation
and parseable as data.

## When to use markdowndata

- Configuration files that humans will read and edit
- Structured data that should also serve as documentation
- Any place you'd use YAML/JSON but want better readability

## Core concept

A `.md` file with headers becomes a nested dictionary. Each header is a key; the content under that header is the value.

```markdown
# name

Alice

# scores

| subject | grade |
|---------|-------|
| math    | 95    |
| english | 88    |
```

Parses to:

```python
{
    "name": "Alice",
    "scores": [
        {"subject": "math", "grade": 95},
        {"subject": "english", "grade": 88}
    ]
}
```

## What to do next

- **Creating a new config file** → use `workflows/define-config`
- **Adding or editing values in an existing config** → use `workflows/update-values`
- **Looking up syntax for a specific value type** → use `reference/syntax`
- **Looking up the Python API** → use `reference/api`
