from bot.views import app


class TestView:

    @classmethod
    def setup_class(cls):
        cls.client = app.test_client()
        cls.parameters = ["openclassrooms", "paris"]

    def test_route_default(self):
        response = self.client.get("/")
        assert response.status_code == 200

    def test_route_index(self):
        response = self.client.get("/index/")
        assert response.status_code == 200

    def test_route_time(self):

        # def mockreturn(self):
        #     pass
        #
        # monkeypatch.setattr(self.client, "post", mockreturn)
        response = self.client.post("/data")
        assert response.status_code == 500
        # TODO: FIX THIS SHIT!!! needs to not call maps when tested. HOW??
