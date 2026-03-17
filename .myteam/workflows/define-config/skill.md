---
name: define-config
description: How to create a new .md config file using markdowndata
---

# Define a markdowndata Config File

Use this workflow when creating a new `.md` file that will be parsed by `markdowndata`.

## When to use markdowndata instead of YAML/JSON

- The config will be read by humans as documentation
- Values include rich text, tables, or lists that are nicer in Markdown
- You want version-controlled config that is diff-friendly and readable on GitHub

## Step 1: Choose your top-level keys

Each top-level key becomes a `#` (H1) header. Use short, descriptive names.

```markdown
# name

# version

# settings
```

## Step 2: Choose the value type for each key

Pick the value type that best fits the data:

| Data shape                          | Value type to use       |
|-------------------------------------|-------------------------|
| Key-value pairs (structured object) | YAML dict (`===` block) |
| Rows of records                     | MD table                |
| Simple list of items                | MD list                 |
| Any text, prose, or mixed content   | MD text                 |

See `reference/syntax` for full examples of each type.

## Step 3: Write the content under each header

Place a blank line between the header and the content.

```markdown
# name

Alice

# scores

| subject | grade |
|---------|-------|
| math    | 95    |
| english | 88    |

# settings

===
debug: false
max_retries: 3
===
```

## Step 4: Add nesting with sub-headers

Use `##` for nested keys under a `#` section, `###` under `##`, etc.

```markdown
# database

## host

localhost

## port

5432

## credentials

===
user: admin
password: secret
===
```

Parses to:

```python
{
    "database": {
        "host": "localhost",
        "port": 5432,
        "credentials": {"user": "admin", "password": "secret"}
    }
}
```

## Non-negotiables

- **Do not mix headless and with-header styles** in the same file. Either all top-level content has `#` headers, or the
  entire file is headless (one value type, no headers at all).
- **One blank line** between a header and its content.
- **Headers inside fenced code blocks** (` ``` `) are ignored by the parser — they will not become keys.
- **Sub-headers only nest one level at a time** — don't jump from `#` to `###`.

## Full example

**Input (`config.md`):**

```markdown
# project

My Awesome App

# authors

- Alice
- Bob

# metadata

===
version: 1.2.0
stable: true
===

## tags

- python
- config
- markdown
```

**Output:**

```python
{
    "project": "My Awesome App",
    "authors": ["Alice", "Bob"],
    "metadata": {
        "content": {"version": "1.2.0", "stable": True},
        "tags": ["python", "config", "markdown"]
    }
}
```

## Step 5: Verify

After writing the file, load it with Python to confirm the output:

```python
import markdowndata

with open("config.md") as f:
    data = markdowndata.load(f)

print(data)
```
