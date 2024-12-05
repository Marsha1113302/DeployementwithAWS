import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_marshall(client):
    """Test the hello marshall route."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Hello, Everyone!"  

def test_add(client):
    """Test the add route."""
    response = client.get('/add')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "15"  