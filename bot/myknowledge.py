"""Media API call module"""
import json

from urllib import request, error as e

from constants import SEARCH_URL, EXTRACT_URL


class Wiki:
    """Call WikiMedia API and retrieve page extract from response"""

    def __init__(self):
        self.search_url = ""
        self.search_response = {}
        self.pageid = {}
        self.extract_url = ""
        self.extract_response = {}

    def create_search_url(self, parsed_address):
        """Format search URL from parser results

        Args:
            parsed_address: result of parser module on Maps address
        """
        parameters = "%20".join(parsed_address)
        self.search_url = "{}srsearch={}".format(SEARCH_URL, parameters)

    def get_search(self):
        """Call MediaWiki search API and decode response or handle error"""
        try:
            response = request.urlopen(self.search_url)
            self.search_response = json.loads(response.read().decode("utf8"))
        except e.HTTPError as err:
            self.search_response = "INVALID REQUEST. ERROR CODE: {}".format(
                err.code)

    def extract_pageid(self):
        """Extract pageid value from search API repsonse"""
        self.pageid = self.search_response["query"]["search"][0]

    def create_extract_url(self):
        """Construct extract API call URL from pageid"""
        article = self.pageid["pageid"]
        self.extract_url = "{}&pageids={}".format(EXTRACT_URL, article)

    def get_extract(self):
        """Call MediaWiki extract API and decode response or handle error"""
        try:
            response = request.urlopen(self.extract_url)
            self.extract_response = json.loads(response.read().decode("utf8"))
        except e.HTTPError as err:
            self.extract_response = "INVALID REQUEST. ERROR CODE: {}".format(
                err.code)

    def extract_text(self):
        """Extract useful information from API response"""
        if isinstance(self.extract_response, dict):
            page = self.pageid["pageid"]
            response = self.extract_response["query"]["pages"][str(page)]
            if "missing" not in response:
                text = response["extract"]
            else:
                text = "INVALID REQUEST CONTENT"
        else:
            text = self.extract_response
        return text
