from bot.views import app

def test_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
