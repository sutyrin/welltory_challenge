from flask import Flask, abort


def create_app(pytest=False):
    app = Flask(__name__)

    @app.get("/correlation")
    def correlation():
        abort(404)

    @app.post("/calculate")
    def calculate():
        abort(404)

    if pytest:
        @app.get("/live")
        def live():
            return ''

    return app
