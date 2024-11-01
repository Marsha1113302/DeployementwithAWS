import pytest
from app import app  # Adjust the import based on the actual app structure

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    """Test the hello world route."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Hello, World!"
    
    
def test_add(client):
    response = client.get('/add')
    assert response.status_code == 200
    assert response.get_json() == {"result": 15}  # This should pass