from flask import Flask, request


def create_app(pytest=False):
    app = Flask(__name__)

    @app.post("/correlation")
    def correlation():
        return {}

    if pytest:
        @app.get("/live")
        def live():
            return ''

    return app
