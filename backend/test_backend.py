import pytest
import fakeredis

from backend import app as flask_app

# Patch the redis_client in your Flask app to use fakeredis
@pytest.fixture(autouse=True)
def mock_redis(monkeypatch):
    fake_redis = fakeredis.FakeStrictRedis()
    monkeypatch.setattr('backend.redis_client', fake_redis)
    return fake_redis  # Returns the mock in case you need it

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_add_points(client, mock_redis):
    response = client.post('/add_points', json={'club_name': 'Club A', 'points': 10})
    assert response.status_code == 200
    assert mock_redis.zscore('football_clubs', 'Club A') == 10

def test_get_clubs(client, mock_redis):
    expected_ranking = []
    with open('./ranking.txt', 'r') as f:
        for line in f.readlines():
            club_name, points = line.strip().split(',')
            expected_ranking.append({'club_name': club_name, 'points': float(points)})
            client.post('/add_points', json={'club_name': club_name, 'points': float(points)})
    
    response = client.get('/get_clubs')
    assert response.status_code == 200
    assert response.json == expected_ranking
