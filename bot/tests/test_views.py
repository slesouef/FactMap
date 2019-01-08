from bot.views import app


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

    def test_route_time(self):
        response = self.client.post("/data")
        assert response.status_code == 200
