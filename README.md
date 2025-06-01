# MarkdownData

MarkdownData is a Python tool designed to transform markdown tables into json objects, which allows for 
clean and structured data as well as improves data visualization. 

The tool is particularly useful for data which is often being modified such as in educational contexts. 

## Installation

To install MarkdownData, you can use pip:

```bash
pip install markdowndata
```

## Structure

Each header represents a new JSON object key value pair. Header 1 `#` are the highest level keys, and each 
subsequent header level `##`, `###`, etc. represents a nested key within the parent key.

## Supported Values

### **YAML Dictionaries**

<table>
    <thead>
        <tr>
            <th>Markdown</th>
            <th>Result</th>
        </tr>
    </thead>
    <tbody>
<tr>
<td>

```markdown
# Header

---
Key1: Value1
Key2: Value2
Key3: Value3
---
```

</td>
<td>

```json
{
    "Header": {
        "Key1": "Value1",
        "Key2": "Value2",
        "Key3": "Value3"
    }
}
```

</td>
</tr>
</table>

### **MD List**

<table>
    <thead>
        <tr>
            <th>Markdown</th>
            <th>Result</th>
        </tr>
    </thead>
    <tbody>
<tr>
<td>

```markdown
# Header

- Item1
- Item2
- Item3
- Item4
```

</td>
<td>

```json
{
    "Header": [
        "Item1", "Item2",
        "Item3", "Item4"
    ]
}
```

</td>
</tr>
</table>

### **MD Table**

<table>
    <thead>
        <tr>
            <th>Markdown</th>
            <th>Result</th>
        </tr>
    </thead>
    <tbody>
<tr>
<td>

```markdown
# Header

| Name | Age | City        |
|------|-----|-------------|
| John | 30  | New York    |
| Jane | 25  | Los Angeles |
| Doe  | 22  | Chicago     |
```

</td>
<td>

```json
{
    "Header": [
        {"Name": "John", "Age": 30, "City": "New York"},
        {"Name": "Jane", "Age": 25, "City": "Los Angeles"},
        {"Name": "Doe", "Age": 22, "City": "Chicago"}
    ]
}
```

</td>
</tr>
</table>

### **MD String**

<table>
    <thead>
        <tr>
            <th>Markdown</th>
            <th>Result</th>
        </tr>
    </thead>
    <tbody>
<tr>
<td>

```markdown
# Header

This is a simple string.
```

</td>
<td>

```json
{
    "Header": "This is a simple string."
}
```

</td>
</tr>
</table>
