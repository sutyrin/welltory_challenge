import requests


def saves_and_retrieves_simple_data_t(app_url):
    calculate_input = {}
    correlation_input = {}
    correlation_output = {}
    r = requests.post(app_url + '/calculate', json=calculate_input)

    r = requests.post(app_url + '/correlation', json=correlation_input)

    assert r.status_code == 200
    assert r.json() == correlation_output
