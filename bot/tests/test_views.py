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

    def test_route_index(self):
        """Test /index route"""
        response = self.client.get("/index/")
        assert response.status_code == 200

    def test_route_time(self):
        """Test AJAX request route"""
        response = self.client.post("/data")
        assert response.status_code == 200
