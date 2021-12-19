from flask import Flask, flash, redirect, url_for, jsonify, render_template, request
from fastai.vision.all import *
from flask_bootstrap import Bootstrap
import io

app = Flask(__name__)
Bootstrap(app)

@app.route('/api/weather')
@app.route('/api/weathertypes')
def run_weather():
    return render_template('index.html')

@app.route('/api/ver')
def api_ver():
    version = { 'version': '0.1' }
    return jsonify(version)

@app.route('/api/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
                return f"The URL /api/data is accessed directly. Try going to '/api/weathertypes' to submit form"
    if request.method == 'POST':
        if not request.files['u_img']:
                return render_template('data.html', form_data='You did not submit a file')
        else:
                file = request.files['u_img']
                buffer = io.BytesIO()
                file.save(buffer)
                file = buffer.getbuffer().tobytes()	
                learn_inf = load_learner('models/WeatherModel.pkl')
                predict = learn_inf.predict(file)
                return render_template('data.html', form_data=predict)
