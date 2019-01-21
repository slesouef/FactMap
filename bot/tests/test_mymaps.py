import bot.mymaps as script

import urllib.request
import json

from io import BytesIO

from constants import URL

geocode_response = {
           "results" : [
              {
                 "formatted_address" : "7 Cité Paradis, 75010 Paris, France",
                 "geometry" : {
                    "location" : {
                       "lat" : 48.8747578,
                       "lng" : 2.350564700000001
                    },
                 },
              }
           ],
           "status" : "OK"
        }

empty_response = {
   "results" : [],
   "status" : "ZERO_RESULTS"
}


class TestMaps:

    @classmethod
    def setup_class(cls):
        cls.parameters = ["openclassrooms", "paris"]
        cls.map = script.Map()

    def test_create_url(self):
        self.map.create_url(self.parameters)
        for p in self.parameters:
            assert p in self.map.url

    def test_get_geocode(self, monkeypatch):

        def mockreturn(request):
            return BytesIO(json.dumps(geocode_response).encode())

        monkeypatch.setattr(urllib.request, "urlopen", mockreturn)
        assert self.map.get_geocode() == geocode_response

    # server error ==> http 400+
    def test_get_geocode_error(self):
        self.map.url = URL
        response = self.map.get_geocode()
        assert response == "INVALID REQUEST. ERROR CODE: 400"

    def test_extract_map_info(self):
        self.map.extract_map_info(geocode_response)
        assert self.map.map_data["address"] == "7 Cité Paradis, 75010 Paris, " \
                                               "France"
        assert self.map.map_data["coordinates"] == (48.8747578,
                                                    2.350564700000001)

    # empty response ==> http 200 status ZERO RESPONSE
    def test_extract_map_info_empty(self):
        content = self.map.extract_map_info(empty_response)
        assert content == "INVALID REQUEST CONTENT"
