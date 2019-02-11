"""Media API call testing"""
import json

from urllib import request, parse
from io import BytesIO

import bot.myknowledge as script

from constants import URL

# Mock response contains the necessary fields for both search and extract calls.
# The artificial concatenation was necessary to allow for mocking the responses
# to get_text_extract API calls
MOCK_RESPONSE = {
    "query": {
        "search": [
            {"pageid": 5653202,
             }
        ],
        "pages": {
            "5653202": {
                "extract": "La cité Paradis est une voie publique située dans "
                           "le 10e arrondissement de Paris."
            }
        }
    }
}

SEARCH_EMPTY = {
    "query": {
        "search": []
    }
}

EXTRACT_EMPTY = {
    "query": {
        "pages": {
            "0": {
                "missing": ""
            }
        }
    }
}


class TestExtract:
    """Test API call behaviour"""

    @classmethod
    def setup_class(cls):
        """Setup test class with test paser results and load API caller"""
        cls.extract = script.Extract()
        cls.parameter = ["cité", "paradis", "paris", "france"]
        cls.test_pageid = {"id": 5653202}

    def test_get_text_extract(self, monkeypatch):
        """Test the get text from address method"""

        def mockreturn(response):
            """API calls mock"""
            return BytesIO(json.dumps(MOCK_RESPONSE).encode())

        monkeypatch.setattr(request, "urlopen", mockreturn)
        text = self.extract.get_text_extract(self.parameter)
        assert text["wiki"]["extract"] == "La cité Paradis est une voie " \
                                          "publique située dans le 10e " \
                                          "arrondissement de Paris."

    def test_get_text_extract_no_page(self, monkeypatch):
        """Test get text when no page is returned from search"""

        def mockreturn(response):
            """Empty search return mock"""
            return BytesIO(json.dumps(SEARCH_EMPTY).encode())

        monkeypatch.setattr(request, "urlopen", mockreturn)
        text = self.extract.get_text_extract(self.parameter)
        assert text["wiki"]["status"] == "INVALID REQUEST CONTENT"

    def test_create_search_url(self):
        """Test search url construction"""
        search_url = self.extract._create_search_url(self.parameter)
        parameters = [parse.quote(item) for item in self.parameter]
        for item in parameters:
            assert item in search_url

    def test_create_extract_url(self):
        """Test extract API url construction"""
        extract_url = self.extract._create_extract_url(self.test_pageid)
        assert str(self.test_pageid["id"]) in extract_url

    # test call against mediawiki search API
    def test_api_call(self, monkeypatch):
        """Mock test of search API call"""

        def mockreturn(response):
            """Mock of response to the urllib.request method"""
            return BytesIO(json.dumps(MOCK_RESPONSE).encode())

        monkeypatch.setattr(request, "urlopen", mockreturn)
        response = self.extract._api_call("url")
        assert response == MOCK_RESPONSE

    # test Media wiki API server error : http code 400+
    def test_api_call_error(self):
        """Server error HTTP response code handling test """
        response = self.extract._api_call(URL)
        assert response == "INVALID REQUEST. ERROR CODE: 400"

    def test_extract_pageid(self):
        """Test method for extracting pageid from API response"""
        pageid = self.extract._extract_pageid(MOCK_RESPONSE)
        assert pageid["id"] == self.test_pageid["id"]

    # empty response ==> http 200 status
    def test_extract_pageid_empty(self):
        """Test empty results from API"""
        pageid = self.extract._extract_pageid(SEARCH_EMPTY)
        assert pageid["status"] == "INVALID REQUEST CONTENT"

    def test_extract_pageid_server_error(self):
        """Test server error handling in response parsing"""
        pageid = self.extract._extract_pageid("INVALID REQUEST. ERROR CODE: 400")
        assert pageid["status"] == "INVALID REQUEST. ERROR CODE: 400"

    def test_extract_text(self):
        """Test method for extracting extract text from API response"""
        text = self.extract._extract_text(self.test_pageid, MOCK_RESPONSE)
        assert text["extract"] == "La cité Paradis est une voie publique " \
                                  "située dans le 10e arrondissement de Paris."

    # empty response ==> http 200 status
    def test_extract_text_empty(self):
        """Test empty results from API"""
        pageid = {"id": 0}
        text = self.extract._extract_text(pageid, EXTRACT_EMPTY)
        assert text["status"] == "INVALID REQUEST CONTENT"

    def test_extract_text_server_error(self):
        """Test server error handling in response parsing"""
        text = self.extract._extract_text(self.test_pageid,
                                          "INVALID REQUEST. ERROR CODE: 400")
        assert text["status"] == "INVALID REQUEST. ERROR CODE: 400"
