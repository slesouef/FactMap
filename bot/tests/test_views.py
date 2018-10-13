from bot.views import app


def test_route_default():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200


def test_route_index():
    client = app.test_client()
    response = client.get('/index/')
    assert response.status_code == 200


def test_title():
    client = app.test_client()
    response = client.get('/')
    rv = response.get_data(as_text=True)
    assert 'FactMaps - infobot' in rv


def test_header():
    client = app.test_client()
    response = client.get('/index/')
    rv = response.get_data(as_text=True)
    assert '<header>' in rv
