#! usr/bin/env python3
# -*- coding:utf-8 -*-
import urllib.request
import json

from constants import URL, APIKEY


class Map:

    def create_url(self, parsed_location):
        parameters = "+".join(parsed_location)
        call = "{}address={}&key={}".format(URL, parameters, APIKEY)
        return call

    def get_geocode(self, url):
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode("utf8"))
        return data
    # TODO: error handling
