# MarkData

MarkData is a Python tool designed to transform markdown tables into json objects, which allows for 
clean and structured data as well as improves data visualization. 

The tool is particularly useful for data which is often being updated such as in educational contexts. 

## Structure

 - **h1** Marks the start of a new key value pair in the JSON object
   - It will be followed by a table with the key-value pairs, 
     it will consist of the same key value pairs for each subsequent h1
 - **h2** These can be used as a list of dictionary values under the h1 key

## Example

<table>
    <thead>
        <tr>
            <th>Structure</th>
            <th>Result</th>
        </tr>
    </thead>
    <tbody>
<tr>
<td>

```markdown

# Day 1

| Title | Description |
|-------|-------------|
| foo   | bar         |

## Video

| Title | Description |         Url         |
|-------|-------------|---------------------|
| foo   | bar         | https://example.com |
| baz   | qux         | https://example.com |
| quux  | quuz        | https://example.com |

## Links

| Title |         Url         |
|-------|---------------------|
| foo   | https://example.com |
| bar   | https://example.com |

# Day 2

| Title | Description |
|-------|-------------|
| foo   | bar         |

## Links

| Title |         Url         |
|-------|---------------------|
| bar   | https://example.com |

# Day 3

| Title | Description |
|-------|-------------|
| foo   | bar         |

## Video

| Title | Description |         Url         |
|-------|-------------|---------------------|
| baz   | qux         | https://example.com |
| quux  | quuz        | https://example.com |
```
</td>
<td>

```json
{
  "Day 1": {
    "Title": "foo",
    "Description": "bar",
    "Video": [
      {
        "Title": "foo",
        "Description": "bar",
        "Url": "https://example.com"
      },
      {
        "Title": "baz",
        "Description": "qux",
        "Url": "https://example.com"
      },
      {
        "Title": "quux",
        "Description": "quuz",
        "Url": "https://example.com"
      }
    ],
    "Links": [
      {
        "Title": "foo",
        "Url": "https://example.com"
      },
      {
        "Title": "bar",
        "Url": "https://example.com"
      }
    ]
  },
  "Day 2": {
      "Title": "foo",
      "Description": "bar",
      "Links": [
      {
          "Title": "bar",
          "Url": "https://example.com"
      }
      ]
  },
  "Day 3": {
    "Title": "foo",
    "Description": "bar",
    "Video": [
      {
        "Title": "baz",
        "Description": "qux",
        "Url": "https://example.com"
      },
      {
        "Title": "quux",
        "Description": "quuz",
        "Url": "https://example.com"
      }
    ]
  }
}
```

</td>
</tr>
</table>



