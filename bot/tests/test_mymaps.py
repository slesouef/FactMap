"""Google API call test module"""
import json

from urllib import request, parse
from io import BytesIO

import bot.mymaps as script

from constants import URL

GEOCODE_RESPONSE = {
    "results": [
        {
            "formatted_address": "7 Cité Paradis, 75010 Paris, France",
            "geometry": {
                "location": {
                    "lat": 48.8747578,
                    "lng": 2.350564700000001
                },
            },
        }
    ],
    "status": "OK"
}

EMPTY_RESPONSE = {
    "results": [],
    "status": "ZERO_RESULTS"
}


class TestMaps:
    """Test the API call behaviour"""

    @classmethod
    def setup_class(cls):
        """Setup test class with test parser result and load API caller"""
        cls.parser_results = ["openclassrooms", "paris"]
        cls.map = script.Map()

    def test_get_map_info(self):
        """Test method creating map info dictionary from parsed results"""
        map_data = self.map.get_map_data(self.parser_results)
        assert map_data["status"] == "INVALID REQUEST CONTENT"

    def test_create_url(self):
        """Test the API URL construction from the parser results"""
        url = self.map._create_url(self.parser_results)
        parameters = [parse.quote(p) for p in self.parser_results]
        for item in parameters:
            assert item in url

    def test_get_geocode(self, monkeypatch):
        """Mocked test of the call against API server"""

        def mockreturn(response):
            """Mock of response to the urllib.request method"""
            return BytesIO(json.dumps(GEOCODE_RESPONSE).encode())

        monkeypatch.setattr(request, "urlopen", mockreturn)
        assert self.map._get_geocode("url") == GEOCODE_RESPONSE

    # server error ==> http 400+
    def test_get_geocode_error(self):
        """Test of call method error handling using endpoint w/o parameters"""
        response = self.map._get_geocode(URL)
        assert response == "INVALID REQUEST. ERROR CODE: 400"

    def test_extract_map_info(self):
        """Test of API response treatment"""
        map_data = self.map._extract_map_info(GEOCODE_RESPONSE)
        assert map_data["address"] == "7 Cité Paradis, 75010 Paris, " \
                                               "France"
        assert map_data["coordinates"] == (48.8747578, 2.350564700000001)

    # empty response ==> http 200 status ZERO RESPONSE
    def test_extract_map_info_empty(self):
        """Test of empty result response from API"""
        map_data = self.map._extract_map_info(EMPTY_RESPONSE)
        assert map_data["status"] == "INVALID REQUEST CONTENT"

    def test_extract_map_info_server_error(self):
        """Test of server error case on API call"""
        response = self.map._get_geocode(URL)
        map_data = self.map._extract_map_info(response)
        assert map_data["status"] == "INVALID REQUEST. ERROR CODE: 400"
