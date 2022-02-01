import requests as requests

def returns_404__if_no_data_present_t(app_url, simple_input):
    r = requests.get(app_url.correlation, params=simple_input)

    assert r.status_code == 404


def calls_correlation_engine__if_called_t(app_url, simple_input, correlation_engine):
    r = requests.get(app_url.correlation, params=simple_input)

    correlation_engine.assert_called_once()
