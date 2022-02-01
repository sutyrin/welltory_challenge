import requests as requests


def returns_404__if_requested_invalid_url_t(app_url):
    r = requests.get(str(app_url) + '/invalid')

    assert r.status_code == 404


def returns_200__if_requested_liveness_url_t(app_url):
    r = requests.get(app_url.live)

    assert r.status_code == 200
