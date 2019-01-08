from bot.views import app


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


class TestView:

    @classmethod
    def setup_class(cls):
        cls.client = app.test_client()

    def test_route_default(self):
        response = self.client.get("/")
        assert response.status_code == 200

    def test_route_index(self):
        response = self.client.get("/index/")
        assert response.status_code == 200

    def test_route_time(self, monkeypatch):
        response = self.client.post("/data")
        assert response.status_code == 200
