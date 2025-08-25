import json
from pathlib import Path
from textwrap import dedent

import markdowndata

TESTS = Path("test_files")


def build_test(
        expected_data_file: str = None,
        expected_data=None,
        input_file: str = None,
        input_string: str = None
):
    if input_file:
        with open(TESTS / input_file) as file:
            data = markdowndata.load(file)
    elif input_string:
        input_string = dedent(input_string)
        data = markdowndata.loads(input_string)
    else:
        raise ValueError("Either input_file or input_string must be provided")

    # Load the expected data
    if expected_data is None and not expected_data_file:
        raise ValueError("Either expected_data or expected_data_file must be provided")

    if expected_data is None:
        with open(TESTS / expected_data_file) as expected_output_file:
            expected_data = json.load(expected_output_file)

    # Compare the loaded data with the expected data
    assert data == expected_data, f"Loaded data from {input_file} does not match expected data from {expected_output_file}"
