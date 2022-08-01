from flask import Flask, request
from flask_cors import CORS
from utils import get_json
settings = get_json("./data", "server")
index = "index.html"




def request_handler():
    if request.method == "POST":
        return request.form.to_dict()
    else:
        query_string = list(filter(
            lambda i: len(i) == 2, [
                s.split("=") for s in request.query_string.decode("utf-8").split("&")
            ]
        ))
        return {
            x[0]: x[1] for x in query_string
        }


def init_app():
    app = Flask("app")
    CORS(app)
    app.config.update(settings["environment"])
    return app


def run(app):
    app.run(**settings["server"])
    return
