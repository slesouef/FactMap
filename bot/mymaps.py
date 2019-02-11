#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""Google Maps module

Responsible for the call to Google Maps geocode API and the treatment of the
response
"""
import os
import json

from urllib import request, parse, error as e

from constants import URL


class Map:
    """Call Google Maps API and extract pertinent information from response"""

    def get_map_data(self, parsed_results):
        """Get API map data

        Args:
            parsed_results: result of Parser module
        """
        url = self._create_url(parsed_results)
        response = self._get_geocode(url)
        map_data = self._extract_map_info(response)
        return map_data

    def _create_url(self, parsed_location):
        """Format call URL from parser result

        Args:
            parsed_location: result of Parser module
        """
        parameters = "+".join(parsed_location)
        safe_parameters = parse.quote(parameters)
        # retrieve API key from environment variable
        apikey = os.getenv("GMAPS_KEY")
        url = "{}address={}&key={}".format(URL, safe_parameters, apikey)
        return url

    def _get_geocode(self, url):
        """Call Google Maps API and decode response or handle error

        Args:
            url: API call url
        """
        try:
            response = request.urlopen(url)
            data = json.loads(response.read().decode("utf8"))
            return data
        except e.HTTPError as err:
            error = "INVALID REQUEST. ERROR CODE: {}".format(err.code)
            return error

    def _extract_map_info(self, api_response):
        """Extract useful information from API response

        Args:
            api_response: content of API response
        """
        response = api_response
        map_data = {}
        if isinstance(response, dict):
            if response["status"] == "OK":
                map_data["status"] = response["status"]
                map_data["address"] = response["results"][0]["formatted_address"]
                latitude = response["results"][0]["geometry"]["location"]["lat"]
                longitude = response["results"][0]["geometry"]["location"]["lng"]
                map_data["coordinates"] = (latitude, longitude)
            else:
                map_data["status"] = "INVALID REQUEST CONTENT"
        else:
            map_data["status"] = response
        return map_data
