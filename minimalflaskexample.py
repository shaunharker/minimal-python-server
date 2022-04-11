#!/usr/bin/python

from flask import Flask, render_template, url_for

app = Flask(__name__.split('.')[0])

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
