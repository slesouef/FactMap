#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""Google Maps module

Responsible for the call to Google Maps geocode API and the treatment of the
response
"""
import os
import json
from urllib import request, error as e

from constants import URL


class Map:
    """Call Google Maps API and extract pertinent information from response"""

    def __init__(self):
        self.map_data = {}
        self.url = ""

    def get_map_data(self, parsed_results):
        """Get API map data

        Args:
            parsed_results: result of parser module
        """
        self.create_url(parsed_results)
        response = self.get_geocode()
        self.extract_map_info(response)

    def create_url(self, parsed_location):
        """Format call URL from parser result

        Args:
            parsed_location: result of Parser module
        """
        parameters = "+".join(parsed_location)
        # retrieve API key from environment variable
        apikey = os.getenv("GMAPS_KEY")
        self.url = "{}address={}&key={}".format(URL, parameters, apikey)

    def get_geocode(self):
        """Call Google Maps API and decode response or handle error"""
        try:
            response = request.urlopen(self.url)
            data = json.loads(response.read().decode("utf8"))
            return data
        except e.HTTPError as err:
            error = "INVALID REQUEST. ERROR CODE: {}".format(err.code)
            return error

    def extract_map_info(self, api_response):
        """Extract useful information from API response

        Args:
            api_response: content of API response
        """
        response = api_response
        if isinstance(response, dict):
            if response["status"] == "OK":
                self.map_data["status"] = response["status"]
                self.map_data["address"] = response["results"][0]["formatted_address"]
                latitude = response["results"][0]["geometry"]["location"]["lat"]
                longitude = response["results"][0]["geometry"]["location"]["lng"]
                self.map_data["coordinates"] = (latitude, longitude)
            else:
                self.map_data["status"] = "INVALID REQUEST CONTENT"
        else:
            self.map_data["status"] = response
