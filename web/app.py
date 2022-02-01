import os

from flask import Flask, abort

data = None
correlation_engine = None


def create_app(_correlation_engine=None):
    app = Flask(__name__)
    global correlation_engine
    correlation_engine = _correlation_engine

    @app.get("/correlation")
    def correlation():
        correlation_engine()
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
