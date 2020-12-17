from flask import Flask, render_template, redirect, request
import cv2
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate',130)
from random import randint
def get_val():
    return randint(0,1000)

import Caption_it

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template("index.html")

@app.route('/',methods = ['POST'])
def caption():
	if request.method == 'POST':
		x = get_val()
		cap = cv2.VideoCapture("http://192.168.0.106:8080/video")
		ret,frame = cap.read()
		#cv2.imshow('img1',frame)
		path = ("static/c{}.png".format(x))
		cv2.imwrite(path,frame)
		cv2.destroyAllWindows()
		cap.release()
		caption = Caption_it.caption_this_image(path)
		engine.say(caption)
		engine.runAndWait()
		result_dic = {
			'image' : path,
			'caption' : caption
		}

	return render_template("index.html",your_result = result_dic)

if __name__ == '__main__':
	app.run(debug=False,threaded = False)
