from flask import render_template, redirect, url_for
from application import app
import requests

@app.route('/', methods=['GET'])
def layout():
        return render_template('layout.html', title='Home')

@app.route('/get/animal', methods = ['GET', 'POST'])
def animal():
	animal = requests.get('http://service2:5001/animal/name')
	noise = requests.post('http://service2:5001/animal/noise', data=animal.text)
	return render_template('animals.html', title="Animals", animal=animal.text, noise=noise.text)
