"""Media API call testing"""
import urllib.request
import json

from io import BytesIO

import bot.myknowledge as script

from constants import URL


SEARCH_RESPONSE = {
    "query": {
        "search": [
            {
                "pageid": 5653202,
            }
        ]
    }
}

    # extract api stub
    # {
    #     "query":{
    #         "pages":{
    #             "5653202":{
    #                 "extract":"La cité Paradis est une voie publique située
#                              \ dans le 10e arrondissement de Paris."
    #             }
    #         }
    #     }
    # }


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


    # test call against media wiki search API
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


# test extract url construction
    # get pageid from search call repsonse
    # create extract url
    # https://fr.wikipedia.org/w/api.php?action=query&format=json&prop=extracts \
    #                                    &exintro=&utf8=1&explaintext=1 \
    #                                    &pageids=5653202

# test response to client
    # test extract response from API
    # test reponse sent to client
