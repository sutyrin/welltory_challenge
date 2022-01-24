import requests as requests


def returns_404__if_requested_invalid_url_t(base_url):
    r = requests.get(base_url + '/invalid')

    assert r.status_code == 404
    assert False, 'wip'
