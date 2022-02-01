class AppURL:
    def __init__(self, base_url, flask_app):
        self.base_url = base_url
        self.flask_app = flask_app

    @property
    def calculate(self):
        return self.base_url + '/calculate'

    @property
    def correlation(self):
        return self.base_url + '/correlation'

    @property
    def live(self):
        return self.base_url + '/live'

    def __str__(self):
        return self.base_url + '/'

    def test_client(self):
        return self.flask_app.test_client()
