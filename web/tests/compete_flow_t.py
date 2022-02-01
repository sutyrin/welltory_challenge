import requests


def saves_and_retrieves_simple_data_t(
    app_url, calculate_input, correlation_input, correlation_output,
):
    requests.post(app_url.calculate, json=calculate_input)

    r = requests.get(app_url.correlation, params=correlation_input)

    assert r.status_code == 200
    assert r.json() == correlation_output
