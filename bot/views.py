from flask import Flask, render_template, request, jsonify
from bot.myparser import Parser
from bot.mymaps import Map
from constants import DATA


app = Flask(__name__)


@app.route("/")
@app.route("/index/")
def index():
    return render_template("index.html")


@app.route("/data", methods=["POST"])
def parse():
    myparser = Parser(DATA)
    mymap = Map()
    entry = request.data.decode()
    myparser.list_creation(entry)
    location = myparser.parse_list()
    url = mymap.create_url(location)
    data = mymap.get_geocode(url)
    mymap.extract_map_info(data)
    return jsonify(mymap.map_data)
