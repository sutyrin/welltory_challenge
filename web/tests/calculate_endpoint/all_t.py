def returns_404__if_no_data_present_t(app_url, not_present_input):
    r = app_url.test_client().post(app_url.calculate, data=not_present_input)

    assert r.status_code == 404
