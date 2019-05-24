from flask import Flask, abort, render_template

app = Flask(__name__)


@app.route('/log')
def login():
    abort(401)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
