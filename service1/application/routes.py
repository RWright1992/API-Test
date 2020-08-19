from flask import render_template, redirect, url_for
from application import app
import requests

@app.route('/')
@app.route('/layout')
def layout():
        return render_template('layout.html', title='Home')

@app.route('/request')
def route():

	r = requests.get('http://service2:5000')

	return r.text


