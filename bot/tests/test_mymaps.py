import bot.mymaps as script

import requests



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

    def test_geocode_request(self, monkeypatch):
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

        def mockreturn(request):
            return geocode_response

        monkeypatch.setattr(requests, 'get', mockreturn)
        assert self.map.get_geocode() == geocode_response

# TODO: test error cases (empty response, server error, ...)
# TODO: test ajax response
