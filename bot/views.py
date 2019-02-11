#! usr/bin/env python3
"""main flask module

responsible to launch Flask server
responsible for the render of the bot web page
responsible for the response to the ajax call
"""
from flask import Flask, render_template, request, jsonify
from bot.myparser import Parser
from bot.mymaps import Map
from bot.myknowledge import Extract



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
    response = {}
    location = Parser().parse(request.data.decode())
    if not location:
        return jsonify({"error": "empty parse return"})
    my_map = Map().get_map_data(location)
    response["map"] = my_map
    if response["map"]["status"] == "OK":
        address = my_map["address"]
        target = Parser().parse(address)
        my_extract = Extract().get_text_extract(target)
        response["wiki"] = my_extract
    return jsonify(response)
