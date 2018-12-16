from flask import Flask, render_template, jsonify
from datetime import datetime


app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/data')
def time():
    return "test ok"
