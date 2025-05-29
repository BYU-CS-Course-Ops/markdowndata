import json
import markdata
from test_utils.test_utils import TESTS


def test_all_value_types_data():
    with open(TESTS / "all_value_types_data.input.md") as file:
        all_value_types_data = markdata.load(file)

    with open(TESTS / "all_value_types_data.expected.json", 'r') as expected_file:
        expected_data = json.load(expected_file)

    # Ensure data is a dict
    assert isinstance(all_value_types_data, dict)

    # Use plain assert for rich diff in pytest
    assert all_value_types_data == expected_data


if __name__ == "__main__":
    test_all_value_types_data()
    print("All tests passed!")
