class AppURL:
    def __init__(self, base_url):
        self.base_url = base_url

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
