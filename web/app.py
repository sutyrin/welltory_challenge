from flask import Flask, request, abort


def create_app(pytest=False):
    app = Flask(__name__)

    @app.post("/correlation")
    def correlation():
        abort(404)

    if pytest:
        @app.get("/live")
        def live():
            return ''

    return app
