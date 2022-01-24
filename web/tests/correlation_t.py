import requests as requests


def returns_right_result_for_simple_case_t(app_url, simple_input, simple_output):
    r = requests.post(app_url + '/correlation', json=simple_input)

    assert r.status_code == 200
    assert r.json() == simple_output
