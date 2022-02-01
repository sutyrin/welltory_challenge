import requests as requests


def returns_404__if_no_data_present_t(app_url, simple_input, simple_output):
    r = requests.post(app_url + '/correlation', json=simple_input)

    assert r.status_code == 404
    # assert r.json() == simple_output
