from flask import Response, request
from application import app
from random import randint

@app.route('/animal/name', methods = ['GET'])
def animal_name():
	animals = ["Dog","Cat","Lion","Cow"]
	return Response(animals[randint(0,3)], mimetype='text/plain')


@app.route('/animal/noise', methods = ['POST'])
def animal_noise():
	animal = request.data.decode("utf-8")
	if animal == "Dog":
		noise = "Woof"
	elif animal == "Cat":
		noise = "Meow"
	elif animal == "Lion":
		noise = "Sleep"
	elif animal == "Cow":
		noise = "I have no clothes"
	else:
		noise = "We do not have this noise"
	return Response(noise, mimetype= 'text/plain')
