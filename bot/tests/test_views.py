"""Flask test module"""
from bot.views import APP


class TestView:
    """Test the Flask endpoints"""

    @classmethod
    def setup_class(cls):
        """Setup Flask test client"""
        cls.client = APP.test_client()

    def test_route_default(self):
        """Test default route"""
        response = self.client.get("/")
        assert response.status_code == 200
        assert b"<!DOCTYPE html>" in response.data

    def test_route_index(self):
        """Test /index route"""
        response = self.client.get("/index/")
        assert response.status_code == 200
        assert b"<!DOCTYPE html>" in response.data

    def test_route_favicon(self):
        """Test favicon.ico route"""
        response = self.client.get("/favicon.ico")
        assert response.status_code == 200

    def test_route_browserconfig(self):
        """Test browserconfig route"""
        response = self.client.get("/browserconfig.xml")
        assert response.status_code == 200

    def test_route_data_parser_error(self):
        """Test AJAX request route without request body"""
        response = self.client.post("/data")
        assert response.status_code == 200
        assert response.data == b'{"error":"empty parse return"}\n'

    def test_route_data_map_error(self):
        """Test AJAX test route with request body"""
        response = self.client.post("/data", data=b"ou se trouve openclassroom"
                                                  b"paris?")
        assert response.status_code == 200
        assert response.data == b'{"map":{"status":"INVALID REQUEST ' \
                                b'CONTENT"}}\n'

# TODO: test successful response path
