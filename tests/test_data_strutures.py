from tests.test_utils import build_test


def test_small_data():
    build_test(
        input_file="small_data.input.md",
        expected_file="small_data.expected.json"
    )


def test_medium_data():
    build_test(
        input_file="medium_data.input.md",
        expected_file="medium_data.expected.json"
    )


def test_md_content_data():
    build_test(
        input_file="md_content_data.input.md",
        expected_file="md_content_data.expected.json"
    )


def test_all_value_types_data():
    build_test(
        input_file="all_value_types_data.input.md",
        expected_file="all_value_types_data.expected.json"
    )


def test_nested_data():
    build_test(
        input_file="nested_data.input.md",
        expected_file="nested_data.expected.json"
    )


def test_complex_data():
    build_test(
        input_file="complex_data.input.md",
        expected_file="complex_data.expected.json"
    )


def test_sample_data():
    build_test(
        input_file="sample_data.input.md",
        expected_file="sample_data.expected.json"
    )
