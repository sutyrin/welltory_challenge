import json
from multiprocessing import Process

import pytest

from web.app import create_app

pytestmark = [
    pytest.mark.integration_test,
]


@pytest.fixture
def port():
    return 5000


@pytest.fixture
def app_url(port):
    a = create_app()
    process = Process(target=a.run, kwargs=dict(port=port))
    process.start()

    yield f'http://localhost:{port}'

    process.terminate()
    process.join()


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
