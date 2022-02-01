import json

import pytest


@pytest.fixture
def simple_input():
    return {
        'x_data_type': 'test',
        'y_data_type': 'test',
    }


@pytest.fixture
def simple_output():
    return json.loads(""" {
        "user_id": 1,
        "x_data_type": "test",
        "y_data_type": "test",
        "correlation": {
            "value": 1.0,
            "p_value": 1.0
        }
    }""")
