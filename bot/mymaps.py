#! usr/bin/env python3
# -*- coding:utf-8 -*-
import urllib.request
import json

from constants import URL, APIKEY


class Map:

    def __init__(self):
        self.map_data = {}

    def create_url(self, parsed_location):
        parameters = "+".join(parsed_location)
        call = "{}address={}&key={}".format(URL, parameters, APIKEY)
        return call

    def get_geocode(self, url):
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode("utf8"))
        return data
    # TODO: error handling

    def extract_map_info(self, data):
        p = data
        if p["status"] == "OK":
            self.map_data["address"] = p["results"][0]["formatted_address"]
            latitude = p["results"][0]["geometry"]["location"]["lat"]
            longitude = p["results"][0]["geometry"]["location"]["lng"]
            self.map_data["coordinates"] = (latitude, longitude)
        else:
            raise Exception("KO status")
