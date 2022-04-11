#!/usr/bin/python3

from flask import Flask

app = Flask(__name__.split('.')[0])

@app.route("/")
def main():
    with open("index.html") as infile:
        data = infile.read()
        return data
