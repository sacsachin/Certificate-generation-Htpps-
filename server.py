#!/usr/bin/env python3

from flask import Flask

MESSAGE = "Private Message!!!"

app = Flask(__name__)

@app.route("/")
def get_secrate_message():
    return MESSAGE + "\n"

if __name__ == "__main__":
    app.run(port=5684,
            ssl_context=("server-public-key.pem", "server-private-key.pem"))
