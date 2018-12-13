from flask import Flask, render_template, request, session, redirect, url_for, session
from flask_bootstrap import Bootstrap
from api import get_prob
import numpy as np
from flask_wtf import FlaskForm
from wtforms import (StringField, RadioField, DecimalField, SubmitField)
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime
from sklearn.model_selection import train_test_split, RandomizedSearchCV, GridSearchCV

''''
For Prediction
'''
import pandas as pd
import numpy as np
import pickle
from sklearn.externals import joblib

app = Flask('Twitch Plays')
Bootstrap(app)

@app.route('/', methods = ['POST', 'GET'])
def index():
	if request.method == 'GET':
		return render_template('index.html')

@app.route('/demo', methods = ['POST', 'GET'])
def prediction_input():
	return render_template('demo.html')

@app.route('/pred', methods = ['GET', 'POST'])
def prediction_graph():
	print('I did something?')
	prob = get_prob()
	# return render_template('eat.html', state = 'Louisiana')
	return render_template('pred.html', state = 'Louisiana', prob = prob)

if __name__ == "__main__":
    app.run(debug=True)



