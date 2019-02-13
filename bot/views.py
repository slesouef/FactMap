#! usr/bin/env python3
"""main flask module

responsible to launch Flask server
responsible for the render of the bot web page
responsible for the response to the ajax call
"""
import os

from flask import Flask, render_template, request, jsonify, send_from_directory
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


@APP.route("/favicon.ico")
def favicon():
    """retuns the favicon from static/img"""
    return send_from_directory(os.path.join(APP.root_path, "static"),
                               "img/favicon.ico",
                               mimetype="image/vnd.microsoft.icon")


@APP.route("/browserconfig.xml")
def browserconfig():
    """returns browserconfig.xml from static folder"""
    return send_from_directory(os.path.join(APP.root_path, "static"),
                               "browserconfig.xml", mimetype="text/xml")


@APP.route("/data", methods=["POST"])
def response():
    """takes the data from POST and creates the response from backend
    treatment"""
    response_data = {}
    location = Parser().parse(request.data.decode())
    if not location:
        return jsonify({"error": "empty parse return"})
    my_map = Map().get_map_data(location)
    response_data["map"] = my_map
    if response_data["map"]["status"] == "OK":
        address = my_map["address"]
        target = Parser().parse(address)
        my_extract = Extract().get_text_extract(target)
        response_data["wiki"] = my_extract
    return jsonify(response_data)
