import bot.mymaps as script

import requests


def test_geocode_request(monkeypatch):
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
    assert script.get_geocode() == geocode_response

# TODO: create test class
# TODO: test call to gmaps (from parser content)
# TODO: test response from gmaps stub
# TODO: test error cases (empty response, server error, ...)
# TODO: test ajax response
