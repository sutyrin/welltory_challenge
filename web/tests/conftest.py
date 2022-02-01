from multiprocessing import Process

import pytest

from web.app import create_app
from web.tests.utils import AppURL

pytestmark = [
    pytest.mark.integration_test,
]


@pytest.fixture
def port():
    return 5000


@pytest.fixture
def app_url(port):
    a = create_app()
    process = Process(target=a.run, kwargs={'port': port})
    process.start()

    yield AppURL(f'http://localhost:{port}')

    process.terminate()
    process.join()


@pytest.fixture
def calculate_input():
    return {
        'user_id': 1,
        'data': {
            'x_data_type': 'sleep',
            'y_data_type': 'eat',
            'x': [
                {'date': '2022-02-01', 'value': 1.0},
            ],
            'y': [
                {'date': '2022-02-01', 'value': 1.0},
            ],
        },
    }


@pytest.fixture
def correlation_input():
    return {
        'x_data_type': 'sleep',
        'y_data_type': 'eat',
    }


@pytest.fixture
def correlation_output():
    return {
        'user_id': 1,
        'x_data_type': 'sleep',
        'y_data_type': 'eat',
        'correlation': {
            'value': 1.0,
            'p_value': 1.0,
        },
    }
