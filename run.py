import os
from flask import Flask, redirect

app = Flask(__name__)

messages = []


def add_messages(username, message):
    """Add messages to the messages list"""
    messages.append("{}: {}".format(username, message))


def get_all_messages():
    """Get all the messages and separate them with a 'br'"""
    return "<br>".join(messages)


@app.route('/')
def index():
    """ Main page with instructions """
    return "To send a message use /USERNAME/MESSAGE"


@app.route('/<username>')
def user(username):
    """ Display chat messages """
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())


@app.route('/<username>/<message>')
def send_message(username, message):
    """ Create a new message and redurect back to chat page """
    add_messages(username, message)
    return redirect("/" + username)


# This is the way the lesson showed but it VS throws an error saying port has to be a str instead of int
# app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
if __name__ == "__main__":
    app.run(host=os.getenv("IP"),
            port=(os.getenv("PORT")),
            debug=True)
