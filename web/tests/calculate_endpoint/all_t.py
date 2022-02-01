import requests as requests


def returns_404__if_no_data_present_t(app_url, not_present_input):
    r = requests.post(app_url + '/calculate', json=not_present_input)

    assert r.status_code == 404
