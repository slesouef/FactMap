import bot.mymaps as script

import urllib.request
import json

from io import BytesIO

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


class TestMaps:

    @classmethod
    def setup_class(cls):
        cls.parameters = ["openclassrooms", "paris"]
        cls.map = script.Map()
        cls.url = ""

    def test_create_url(self):
        self.url = self.map.create_url(self.parameters)
        for p in self.parameters:
            assert p in self.url

    def test_get_geocode(self, monkeypatch):

        def mockreturn(request):
            return BytesIO(json.dumps(geocode_response).encode())

        monkeypatch.setattr(urllib.request, "urlopen", mockreturn)
        assert self.map.get_geocode("") == geocode_response

# TODO: test error cases (empty response, server error, ...)

    def test_extract_map_info(self):
        self.map.extract_map_info(geocode_response)
        assert self.map.map_data["address"] == "7 Cité Paradis, 75010 Paris, " \
                                               "France"
        assert self.map.map_data["coordinates"] == (48.8747578,
                                                    2.350564700000001)
