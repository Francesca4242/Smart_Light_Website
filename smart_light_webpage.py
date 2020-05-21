# importing the requests library 
import requests 
import math
import random
from random import randint
import threading
from threading import Thread
import time
from flask import Flask, render_template, request
app = Flask("MyApp")


  
# api-endpoint 
URL = "http://192.168.86.222/cm"

def unicorn_vomit_light(value):
	# do something that takes a long time
	for x in range(150000000):

		# location given here 
		light=1
		red_num=randint(0,255)
		green_num=randint(0,255)
		blue_num=randint(0,255)
		white_num=0
		red=format(int(red_num), 'x').zfill(2)
		green=format(int(green_num), 'x').zfill(2)
		blue=format(int(blue_num), 'x').zfill(2)
		white=format(white_num, 'x').zfill(2)

		# defining a params dict for the parameters to be sent to the API 
		PARAMS = {'cmnd':'color '+red+green+blue+white} 
		  
		# sending get request and saving the response as response object 
		r = requests.get(url = URL, params = PARAMS) 

		print(r.url)

def steady_rainbow_light(value):
	frequency = .3
	for i in range(150000000):

		# location given here 
		light=1
		red_num=math.sin(frequency*i + 0) * 127 + 128
		green_num=math.sin(frequency*i + 2) * 127 + 128;
		blue_num=math.sin(frequency*i + 4) * 127 + 128;
		white_num=0
		red=format(int(red_num), 'x').zfill(2)
		green=format(int(green_num), 'x').zfill(2)
		blue=format(int(blue_num), 'x').zfill(2)
		white=format(white_num, 'x').zfill(2)

		# defining a params dict for the parameters to be sent to the API 
		PARAMS = {'cmnd':'color '+red+green+blue+white} 
		  
		# sending get request and saving the response as response object 
		r = requests.get(url = URL, params = PARAMS) 

		print(r.url)
		time.sleep(10)
	

@app.route("/unicorn_vomit")
def unicorn_vomit():
	URL = "http://192.168.86.222/cm"
	thread = Thread(target=unicorn_vomit_light, kwargs={'value': request.args.get('value', 20)})
	thread.start()
	return render_template ("light_api.html")
	
	

@app.route("/steady_rainbow")
def steady_rainbow():
	thread = Thread(target=steady_rainbow_light, kwargs={'value': request.args.get('value', 20)})
	thread.start()
	# api-endpoint 
	URL = "http://192.168.86.222/cm"
	#for x in range(100):
	return render_template("light_api.html")

@app.route("/")
def home():
	return render_template ("light_api.html")


app.run(debug=True)