import json

import pytest

@pytest.fixture
def simple_input():
    return json.loads("""{
        "user_id": 1,
        "data": {
            "x_data_type": "test",
            "y_data_type": "test",
            "x": [
                {
                    "date": "2022-01-24",
                    "value": 1.0
                }
            ],
            "y": [
                {
                    "date": "2022-01-24",
                    "value": 1.0
                }
            ]
        }
    }""")


@pytest.fixture
def not_present_input(simple_input):
    return simple_input
