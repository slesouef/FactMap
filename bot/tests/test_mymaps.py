"""Google API call test module"""
import urllib.request
import json

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
        cls.parameters = ["openclassrooms", "paris"]
        cls.map = script.Map()

    def test_create_url(self):
        """Test the API URL construction from the parser results"""
        self.map.create_url(self.parameters)
        for item in self.parameters:
            assert item in self.map.url

    def test_get_geocode(self, monkeypatch):
        """Mocked test of the call against API server"""

        def mockreturn(request):
            """Mock of response to the urllib.request method"""
            return BytesIO(json.dumps(GEOCODE_RESPONSE).encode())

        monkeypatch.setattr(urllib.request, "urlopen", mockreturn)
        assert self.map.get_geocode() == GEOCODE_RESPONSE

    # server error ==> http 400+
    def test_get_geocode_error(self):
        """Test of call method error handling using endpoint w/o parameters"""
        self.map.url = URL
        response = self.map.get_geocode()
        assert response == "INVALID REQUEST. ERROR CODE: 400"

    def test_extract_map_info(self):
        """Test of API response treatment"""
        self.map.extract_map_info(GEOCODE_RESPONSE)
        assert self.map.map_data["address"] == "7 Cité Paradis, 75010 Paris, " \
                                               "France"
        assert self.map.map_data["coordinates"] == (48.8747578,
                                                    2.350564700000001)

    # empty response ==> http 200 status ZERO RESPONSE
    def test_extract_map_info_empty(self):
        """Test of empty result response from API"""
        content = self.map.extract_map_info(EMPTY_RESPONSE)
        assert content == "INVALID REQUEST CONTENT"
