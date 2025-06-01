import json
import markdowndata
from pathlib import Path

TESTS = Path("test_files")

def build_test(input_file: str, expected_file: str):
    # Load the input data
    with open(TESTS / input_file) as file:
        data = markdowndata.load(file)

    # Check if the data is loaded correctly
    assert isinstance(data, dict), f"Loaded data from {input_file} should be a dictionary"

    # Load the expected data
    with open(TESTS / expected_file, 'r') as expected_output:
        expected_data = json.load(expected_output)

    # Compare the loaded data with the expected data
    assert data == expected_data, f"Loaded data from {input_file} does not match expected data from {expected_file}"