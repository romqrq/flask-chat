import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello There!</h1>"

# This is the way the lesson showed but it VS throws an error saying port has to be a str instead of int
# app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)


if __name__ == "__main__":
    app.run(host=os.getenv("IP"),
            port=(os.getenv("PORT")),
            debug=True)
