from flask import redirect, url_for
from application import app
import requests

@app.route('/')
@app.route('/string')
def requestFunction():
    return "def"

