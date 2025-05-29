import json
import markdata
from test_utils.test_utils import TESTS


def test_nested_data():
    # Load the nested data from the markdata package
    with open(TESTS / "nested_data.input.md") as file:
        nested_data = markdata.load(file)

    # Check if the data is loaded correctly
    assert isinstance(nested_data, dict), "Loaded data should be a dictionary"

    with open(TESTS / "nested_data.expected.json", 'r') as expected_file:
        expected_data = json.load(expected_file)

    # Compare the loaded data with the expected data
    assert nested_data == expected_data, "Loaded data does not match expected data"


if __name__ == "__main__":
    test_nested_data()
    print("Test passed successfully!")