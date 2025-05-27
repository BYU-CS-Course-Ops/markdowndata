import json
import markdata
from test_utils.test_utils import TESTS

def test_large_data():
    # Load the small data from the markdata package
    with open(TESTS / "large_data.input.md") as file:
        large_data = markdata.load(file)

    # Check if the data is loaded correctly
    assert isinstance(large_data, dict), "Loaded data should be a dictionary"

    with open(TESTS / "large_data.expected.json", 'r') as expected_file:
        expected_data = json.load(expected_file)

    # Compare the loaded data with the expected data
    assert large_data == expected_data, "Loaded data does not match expected data"

if __name__ == "__main__":
    test_large_data()
    print("Test passed successfully!")