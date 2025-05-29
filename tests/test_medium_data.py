import json
import markdata
from test_utils.test_utils import TESTS


def test_medium_data():
    # Load the medium data from the markdata package
    with open(TESTS / "medium_data.input.md") as file:
        medium_data = markdata.load(file)

    # Check if the data is loaded correctly
    assert isinstance(medium_data, dict), "Loaded data should be a dictionary"

    with open(TESTS / "medium_data.expected.json", 'r') as expected_file:
        expected_data = json.load(expected_file)

    # Compare the loaded data with the expected data
    assert medium_data == expected_data, "Loaded data does not match expected data"


if __name__ == "__main__":
    test_medium_data()
    print("Test passed successfully!")