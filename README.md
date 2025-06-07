# MarkdownData

MarkdownData is a python tool designed to transform Markdown tables into json objects, which allows for 
clean and structured data as well as improves data visualization. 

The tool is particularly useful for data which is often being updated, such as in educational contexts. 

## Installation

To install markdowndata, you can use pip:

```bash
pip install markdowndata
```

## Structure

Each header represents a new key value pair. Header 1 `#` are the highest level keys, and each 
subsequent sub-header level `##`, `###`, etc. represents a nested key within the parent key.

## Supported Values

The MarkdownData tool supports the following markdown structures:

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

===
Key1: Value1
Key2: Value2
Key3: Value3
===
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
        "Item1", "Item2", "Item3", "Item4"
    
    ]
}
```

</td>
</tr>
</table>

### **MD Content**

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

This is a md string with **bold** text and *italic* text.
As well as `inline code` and a [link](https://example.com).
```

</td>
<td>

```json
{
    "Header": "This is a md string with **bold** text and *italic* text. As well as `inline code` and a [link](https://example.com)."
}
```

</td>
</tr>
</table>

## Example Usage

There are two ways to use MarkdownData:
1. **From a String**: You can pass a markdown string directly to the `loads` function.
2. **From a File**: You can read a markdown file and pass its content to the `load` function.

### Markdown String to JSON Object

To convert a markdown string to a JSON object, you can use the following code:

```python
import markdowndata

md_string = """
# name

Foo Bar

# birthdays

| date       | name    |
|------------|---------|
| 2023-01-01 | Alice   |
| 2023-02-02 | Bob     |
| 2023-03-03 | Charlie |

# ice cream

===
location: Dairy Queen
rating: 5
===

## flavors

- chocolate
- vanilla
- strawberry
- mint chocolate chip
"""

data = markdowndata.loads(md_string)
```

Which will result in the following JSON object:

```json
{
  "name": "Foo Bar",
  "birthdays": [
    {
      "date": "2023-01-01",
      "name": "Alice"
    },
    {
      "date": "2023-02-02",
      "name": "Bob"
    },
    {
      "date": "2023-03-03",
      "name": "Charlie"
    }
  ],
  "ice cream": {
    "location": "Dairy Queen",
    "rating": 5,
    "flavors": [
      "chocolate",
      "vanilla",
      "strawberry",
      "mint chocolate chip"
    ]
  }
}
```

### Markdown File to JSON Object

To convert a markdown file to a JSON object, you can use the following code:

```python
import markdowndata

with open('example.md') as file:
    data = markdowndata.load(file)
```

With the above example, if `example.md` contains the following markdown the results will be as follows:

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
# name

Test Dataset

# version 

1.0

# metadata

===
created_by: John Doe
date: "2025-06-01"
===

## tags

- example
- test
- json

# data 
 
| id | value | attribute |
|----|-------|-----------|
| 1  | 10    | blue      |
| 2  | 40    | red       |

# summary

===
total_items: 2
average_values: [25, 35, 45, 50, 65]
===

# notes

- This is a test dataset.
- Values are illustrative.
```

</td>
<td>

```json
{
  "name": "Test Dataset",
  "version": 1.0,
  "metadata": {
    "created_by": "John Doe",
    "date": "2025-06-01",
    "tags": [
      "example", 
      "test", 
      "json"
    ]
  },
  "data": [
    {
      "id": 1,
      "value": 10,
      "attribute": "blue"
    },
    {
      "id": 2,
      "value": 40,
      "attribute": "red"
    }
  ],
  "summary": {
    "total_items": 2,
    "average_values": [
      25, 
      35, 
      45,
      50,
      65
    ]
  },
  "notes": [
    "This is a test dataset.",
    "Values are illustrative."
  ]
}
```

</td>
</tr>
</table>

You can access the data as follows:

```python
print(data['name'])                    # Output: Test Dataset
print(data['version'])                 # Output: 1.0
print(data['metadata']['created_by'])  # Output: John Doe
print(data['summary']['total_items'])  # Output: 2
```

## Additional Supported Values

The MarkdownData tool also supports the following additional structures:

### **Headless YAML Dictionary**

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
===
Key1: Value1
Key2: Value2
Key3: Value3
===
```

</td>
<td>

```json
{
    "Key1": "Value1",
    "Key2": "Value2",
    "Key3": "Value3"
}
```

</td>
</tr>
</table>

### **Headless MD Table**

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
| Name | Age | City        |
|------|-----|-------------|
| John | 30  | New York    |
| Jane | 25  | Los Angeles |
| Doe  | 22  | Chicago     |
```

</td>
<td>

```json
[
    {"Name": "John", "Age": 30, "City": "New York"},
    {"Name": "Jane", "Age": 25, "City": "Los Angeles"},
    {"Name": "Doe", "Age": 22, "City": "Chicago"}
]
```

</td>
</tr>
</table>

### **Headless MD List**

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
- Item1
- Item2
- Item3
- Item4
```

</td>
<td>

```json
[
    "Item1", "Item2", "Item3", "Item4"
    
]
```

</td>
</tr>
</table>

### **Headless MD Content**

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
This is a md string with **bold** text and *italic* text.
As well as `inline code` and a [link](https://example.com).
```

</td>
<td>

```json
"This is a md string with **bold** text and *italic* text. As well as `inline code` and a [link](https://example.com)."
```

</td>
</tr>
</tbody>
</table>

## More Examples

You can find more examples in the [`tests/test_files`](tests/test_files) directory of the repository.

## Things to Note

With the `YAML Dictionaries`, dates which are in the format `YYYY-MM-DD` and not wrapped in quotes will be
converted to a `datetime.date` object. If you want to keep the date as a string, you can wrap it in quotes.