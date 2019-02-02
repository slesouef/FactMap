#! usr/bin/env python3
"""main flask module

responsible to launch Flask server
responsible for the render of the bot web page
responsible for the response to the ajax call
"""
from flask import Flask, render_template, request, jsonify
from bot.myparser import Parser
from bot.mymaps import Map



APP = Flask(__name__)

# Config options
APP.config.from_object("config")


@APP.route("/")
@APP.route("/index/")
def index():
    """renders the webapp landing page"""
    return render_template("index.html")


@APP.route("/data", methods=["POST"])
def response():
    """takes the data from POST and creates the response from backend
    treatment"""
    location = Parser().parse(request.data.decode())
    if not location:
        return jsonify({"error": "empty parse return"})
    mymap = Map()
    mymap.get_map_data(location)
    return jsonify(mymap.map_data)
