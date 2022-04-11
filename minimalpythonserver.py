#!/usr/bin/python

from flask import Flask

app = Flask(__name__.split('.')[0])

@app.route("/")
def main():
    with open("/var/www/html/minimalflaskexample/index.html") as infile:
        data = infile.read()
        return data
