"""Media API call testing"""
import urllib.request
import json

from io import BytesIO

import bot.myknowledge as script

from constants import URL

SEARCH_RESPONSE = {
    "query": {
        "search": [
            {"pageid": 5653202,
             }
        ]
    }
}

SEARCH_EMPTY = {
    "query": {
        "search": []
    }
}

EXTRACT_RESPONSE = {
    "query": {
        "pages": {
            "5653202": {
                "extract": "La cité Paradis est une voie publique située dans "
                           "le 10e arrondissement de Paris."
            }
        }
    }
}

EXTRACT_EMPTY = {
    "query": {
        "pages": {
            "0": {
                "pageid": 0,
                "missing": ""
            }
        }
    }
}


class TestWiki:
    """Test API call behaviour"""

    @classmethod
    def setup_class(cls):
        """Setup test class with test paser results and load API caller"""
        cls.wiki = script.Wiki()
        cls.parameter = ["cité", "paradis", "paris", "france"]

    def test_create_search_url(self):
        """Test search url construction"""
        self.wiki.create_search_url(self.parameter)
        for item in self.parameter:
            assert item in self.wiki.search_url

    # test call against mediawiki search API
    def test_get_search(self, monkeypatch):
        """Mock test of search API call"""

        def mockreturn(response):
            """Mock of response to the urllib.request method"""
            return BytesIO(json.dumps(SEARCH_RESPONSE).encode())

        monkeypatch.setattr(urllib.request, "urlopen", mockreturn)
        self.wiki.get_search()
        assert self.wiki.search_response == SEARCH_RESPONSE

    # test Media wiki API server error : http code 400+
    def test_get_search_error(self):
        """Server error HTTP response code handling test """
        self.wiki.search_url = URL
        self.wiki.get_search()
        assert self.wiki.search_response == "INVALID REQUEST. ERROR CODE: 400"

    def test_extract_pageid(self):
        """Test method for extracting pageid from API response"""
        self.wiki.search_response = SEARCH_RESPONSE
        self.wiki.extract_pageid()
        assert self.wiki.pageid == {"pageid": 5653202}

    # empty response ==> http 200 status
    def test_extract_pageid_empty(self):
        """Test empty results from API"""
        self.wiki.search_response = SEARCH_EMPTY
        self.wiki.extract_pageid()
        assert self.wiki.pageid == "INVALID REQUEST CONTENT"

    def test_extract_pageid_server_error(self):
        """Test server error handling in response parsing"""
        self.wiki.search_response = "INVALID REQUEST. ERROR CODE: 400"
        self.wiki.extract_pageid()
        assert self.wiki.pageid == "INVALID REQUEST. ERROR CODE: 400"

    def test_create_extract_url(self):
        """Test extract API url construction"""
        self.wiki.pageid = {"pageid": 5653202}
        self.wiki.create_extract_url()
        assert str(self.wiki.pageid["pageid"]) in self.wiki.extract_url

    # test call against mediawiki extract API
    def test_get_extract(self, monkeypatch):
        """Mock test of extract API call"""

        def mockreturn(response):
            """Mock of response to the urllib.request method"""
            return BytesIO(json.dumps(EXTRACT_RESPONSE).encode())

        monkeypatch.setattr(urllib.request, "urlopen", mockreturn)
        self.wiki.get_extract()
        assert self.wiki.extract_response == EXTRACT_RESPONSE

    # test Media wiki API server error : http code 400+
    def test_get_extract_error(self):
        """Server error HTTP response code handling test"""
        self.wiki.extract_url = URL
        self.wiki.get_extract()
        assert self.wiki.extract_response == "INVALID REQUEST. ERROR CODE: 400"

    def test_extract_text(self):
        """Test method for extracting extract text from API response"""
        self.wiki.extract_response = EXTRACT_RESPONSE
        extract = self.wiki.extract_text()
        assert extract == "La cité Paradis est une voie publique située dans " \
                          "le 10e arrondissement de Paris."

    # empty response ==> http 200 status
    def test_extract_text_empty(self):
        """Test empty results from API"""
        self.wiki.pageid["pageid"] = 0
        self.wiki.extract_response = EXTRACT_EMPTY
        extract = self.wiki.extract_text()
        assert extract == "INVALID REQUEST CONTENT"

    def test_extract_text_server_error(self):
        """Test server error handling in response parsing"""
        self.wiki.extract_response = "INVALID REQUEST. ERROR CODE: 400"
        extract = self.wiki.extract_text()
        print(extract)
        assert extract == "INVALID REQUEST. ERROR CODE: 400"
