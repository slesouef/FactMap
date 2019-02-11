"""Media API call module"""
import json

from urllib import request, parse, error as e

from constants import SEARCH_URL, EXTRACT_URL


class Extract:
    """Call WikiMedia API and retrieve page extract from response"""

    def get_text_extract(self, parsed_address):
        """Return the wiki text extract from parsed address in a dictionary

        Args:
            parsed_address: result of parser module on Map address
        """
        response = {}
        search = self._create_search_url(parsed_address)
        search_results = self._api_call(search)
        page = self._extract_pageid(search_results)
        if page["status"] != "OK":
            response["wiki"] = page
            return response
        extract_page = self._create_extract_url(page)
        extract_results = self._api_call(extract_page)
        extract = self._extract_text(page, extract_results)
        response["wiki"] = extract
        return response

    def _create_search_url(self, parsed_address):
        """Format search URL from parser results

        Args:
            parsed_address: result of parser module on Maps address
        """
        parameters = " ".join(parsed_address)
        parameters_urlsafe = parse.quote(parameters)
        search_url = "{}&srsearch={}".format(SEARCH_URL, parameters_urlsafe)
        return search_url

    def _create_extract_url(self, pageid):
        """Construct extract API call URL from pageid

        Args:
            pageid: dictionary with mediawiki identifier of the page
            retrieved during search
        """
        search_results = pageid
        target = search_results["id"]
        extract_url = "{}&pageids={}".format(EXTRACT_URL, target)
        return extract_url

    def _api_call(self, url):
        """Call MediaWiki search API and decode response or handle error

        Args:
            url: ULR of the API call
        """
        try:
            api = request.urlopen(url)
            response = json.loads(api.read().decode("utf8"))
        except e.HTTPError as err:
            response = "INVALID REQUEST. ERROR CODE: {}".format(
                err.code)
        return response

    def _extract_pageid(self, response):
        """Extract pageid value from search API response

        Args:
            response: API call server response
        """
        pageid = {}
        if isinstance(response, dict):
            if response["query"]["search"]:
                pageid["status"] = "OK"
                pageid["id"] = response["query"]["search"][0]["pageid"]
            else:
                pageid["status"] = "INVALID REQUEST CONTENT"
        else:
            pageid["status"] = response
        return pageid

    def _extract_text(self, pageid, response):
        """Extract useful information from API response

        Args:
            pageid: mediawiki identifier of the page retrieved in search
            response: API call server response
        """
        search_results = pageid
        target = search_results["id"]
        text = {}
        if isinstance(response, dict):
            result = response["query"]["pages"][str(target)]
            if "missing" not in result:
                text["status"] = "OK"
                text["extract"] = result["extract"]
            else:
                text["status"] = "INVALID REQUEST CONTENT"
        else:
            text["status"] = response
        return text
