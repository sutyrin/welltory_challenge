from flask import Flask, request


def create_app(pytest=True):
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    if pytest:
        @app.get("/live")
        def live():
            return ''

    return app
