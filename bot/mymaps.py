#! usr/bin/env python3
# -*- coding:utf-8 -*-
import requests

from constants import URL, APIKEY


class Map:

    def create_url(self, parsed_location):
        parameters = "+".join(parsed_location)
        call = "{}address={}&key={}".format(URL, parameters, APIKEY)
        return call

    def get_geocode(self):
        url = 'test'
        r = requests.get(url)
        return r
