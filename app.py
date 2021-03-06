from flask import Flask, render_template
import subprocess as sp


app = Flask(__name__)


@app.route('/')
def index():
    sp.call(["sass", "./style/main.sass", "./static/main.css"])
    return render_template("index.html", title="TITLE")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)