import requests as requests


def returns_404__if_requested_invalid_url_t(app_url):
    r = requests.get(app_url + '/invalid')

    assert r.status_code == 404


def returns_200__if_requested_liveness_url_t(app_url):
    r = requests.get(app_url + '/live')

    assert r.status_code == 200


def returns_right_result_for_simple_case_t(app_url, simple_input, simple_output):
    r = requests.post(app_url + '/correlation', json=simple_input)

    assert r.status_code == 200
    assert r.json() == simple_output
