import pytest
from Oba.db_module.db_operations import MysqlDB


@pytest.fixture
def your_instance():
    # Create an instance of YourClass if needed
    return MysqlDB()


@pytest.mark.parametrize("input_data, expected_result", [
    (  # Test case 1: Basic example
            [
                [1, 'Alice', 25],
                [2, 'Bob', 30],
                [3, 'Charlie', 35]
            ],
            [
                [1, 'Alice', '25'],
                [2, 'Bob', '30'],
                [3, 'Charlie', '35']
            ]
    ),
    (  # Test case 2: Empty input
            [],
            []
    ),
    (  # Test case 3: Different data types
            [
                [1, 'Alice', 25.5],
                [2, 'Bob', True],
            ],
            [
                [1, 'Alice', '25.5'],
                [2, 'Bob', 'True'],
            ]
    ),
])
def test_update_datatype_for_a_column(your_instance, input_data, expected_result):
    updated_data = your_instance.update_datatype_for_a_column(input_data)
    assert updated_data == expected_result
