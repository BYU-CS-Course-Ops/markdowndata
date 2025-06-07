import json
import markdowndata
from pathlib import Path

TESTS = Path("test_files")

def build_test(expected_output: str, input_file: str = None, input_string: str = None):
    if input_file:
        with open(TESTS / input_file) as file:
            data = markdowndata.load(file)
    elif input_string:
        data = markdowndata.loads(input_string)
    else:
        raise ValueError("Either input_file or input_string must be provided")

    # Load the expected data
    with open(TESTS / expected_output) as expected_output:
        expected_data = json.load(expected_output)

    # Compare the loaded data with the expected data
    assert data == expected_data, f"Loaded data from {input_file} does not match expected data from {expected_output}"
