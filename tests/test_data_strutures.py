from tests.test_utils import build_test


def test_loads_data():
    build_test(
        input_string="""
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
""",
        expected_output="loads_data.expected.json"
    )


def test_only_yaml_data():
    build_test(
        input_file="only_yaml_data.input.md",
        expected_output="only_yaml_data.expected.json"
    )


def test_only_table_data():
    build_test(
        input_file="only_table_data.input.md",
        expected_output="only_table_data.expected.json"
    )

def test_only_list_data():
    build_test(
        input_file="only_list_data.input.md",
        expected_output="only_list_data.expected.json"
    )


def test_small_data():
    build_test(
        input_file="small_data.input.md",
        expected_output="small_data.expected.json"
    )


def test_medium_data():
    build_test(
        input_file="medium_data.input.md",
        expected_output="medium_data.expected.json"
    )


def test_md_content_data():
    build_test(
        input_file="md_content_data.input.md",
        expected_output="md_content_data.expected.json"
    )


def test_all_value_types_data():
    build_test(
        input_file="all_value_types_data.input.md",
        expected_output="all_value_types_data.expected.json"
    )


def test_nested_data():
    build_test(
        input_file="nested_data.input.md",
        expected_output="nested_data.expected.json"
    )


def test_complex_data():
    build_test(
        input_file="complex_data.input.md",
        expected_output="complex_data.expected.json"
    )


def test_sample_data():
    build_test(
        input_file="sample_data.input.md",
        expected_output="sample_data.expected.json"
    )
