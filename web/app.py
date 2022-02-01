import os

from flask import Flask, abort

data = None


def create_app():
    app = Flask(__name__)

    @app.get("/correlation")
    def correlation():
        if data:
            return {
                'user_id': 1,
                'x_data_type': 'sleep',
                'y_data_type': 'eat',
                'correlation': {
                    'value': 1.0,
                    'p_value': 1.0,
                },
            }
        abort(404)

    @app.post("/calculate")
    def calculate():
        global data
        data = True
        abort(404)

    if 'PYTEST_CURRENT_TEST' in os.environ:
        @app.get("/live")
        def live():
            return ''

    return app
