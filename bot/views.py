from flask import Flask, render_template, request, jsonify
from bot.myparser import Parser
from constants import DATA


app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/data', methods = ['POST'])
def parse():
    myparser = Parser(DATA)
    entry = request.data.decode()
    myparser.list_creation(entry)
    location = myparser.parse_list()
    return jsonify(location)
