import pytest
from app.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'DevOps Enthusiast' in response.data

def test_skills(client):
    response = client.get('/skills')
    assert response.status_code == 200
    assert b'Linux Fundamentals' in response.data

def test_projects(client):
    response = client.get('/projects')
    assert response.status_code == 200
    assert b'Ansible Cluster Setup' in response.data

def test_contact(client):
    response = client.get('/contact')
    assert response.status_code == 200
    assert b'vaibhavi.sugandhi03@gmail.com' in response.data
