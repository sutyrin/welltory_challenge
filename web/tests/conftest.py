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
    a = create_app(pytest=True)
    process = Process(target=a.run, kwargs=dict(port=port))
    process.start()

    yield f'http://localhost:{port}'

    process.terminate()
    process.join()
