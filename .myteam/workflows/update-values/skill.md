---
name: update-values
description: How to add or edit values in an existing markdowndata config file
---

# Update Values in a markdowndata Config File

Use this workflow when modifying an existing `.md` config file.

## Before you start

Load the current file to understand its structure:

```python
import markdowndata

with open("config.md") as f:
    data = markdowndata.load(f)

print(data)
```

## Adding a new top-level key

Add a new `#` header at the end of the file, with a blank line before it:

```markdown
# new_key

value here
```

Do not insert new headers in the middle of an existing section's content.

## Changing a value under an existing key

Find the header and edit the content beneath it. The content ends at the next header of the same or higher level.

**Before:**

```markdown
# version

1.0.0
```

**After:**

```markdown
# version

2.0.0
```

## Adding a nested key under an existing section

Add a sub-header inside the section. If the section currently has direct content (no sub-headers), wrap that content in
a `## content` sub-header first to avoid mixing direct content with sub-headers.

**Before:**

```markdown
# settings

===
debug: false
===
```

**After (adding a nested key):**

```markdown
# settings

## options

===
debug: false
===

## timeout

30
```

## Editing a YAML dict value

Find the `===` block and edit the YAML inside it:

**Before:**

```markdown
# metadata

===
version: 1.0.0
author: Alice
===
```

**After:**

```markdown
# metadata

===
version: 2.0.0
author: Alice
released: 2026-01-15
===
```

## Editing a table

Add, remove, or modify rows. Keep the header row and separator row intact:

```markdown
# scores

| subject | grade |
|---------|-------|
| math    | 95    |
| english | 88    |
| science | 92    |
```

## Editing a list

Add or remove bullet items:

```markdown
# tags

- python
- config
- markdown
- new-tag
```

## Non-negotiables

- **Preserve header hierarchy** — do not change a `##` to `#` or vice versa unless you intend to restructure the
  nesting.
- **Do not mix headless and with-header styles** — if the file uses headers, keep using headers; do not add bare content
  at the top level without a header.
- **One blank line** between a header and its content.
- **YAML blocks need `===` delimiters** on their own lines — do not add YAML inline with other content.

## Verify after changes

Always verify after editing:

```python
import markdowndata

with open("config.md") as f:
    data = markdowndata.load(f)

print(data)
```

If the output doesn't match expectations, check that headers are correctly nested and content types are pure (no mixing
of tables with text, etc.).
