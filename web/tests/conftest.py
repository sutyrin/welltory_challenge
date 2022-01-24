import pytest

pytestmark = [
    pytest.mark.integration_test,
]


@pytest.fixture
def base_url():
    return 'http://localhost:8000'
