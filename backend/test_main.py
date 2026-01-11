from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app, get_db
import models
import pytest

# Test Database Setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

models.Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="module")
def sample_user():
    return {"username": "testuser", "password": "testpassword", "role": "user"}

@pytest.fixture(scope="module")
def admin_user():
    return {"username": "admin", "password": "adminpassword", "role": "admin"}

def test_register_user(sample_user):
    response = client.post("/api/auth/register", json=sample_user)
    assert response.status_code == 200
    assert response.json()["username"] == sample_user["username"]

def test_login_user(sample_user):
    response = client.post("/api/auth/login", data={"username": sample_user["username"], "password": sample_user["password"]})
    assert response.status_code == 200
    assert "access_token" in response.json()
    return response.json()["access_token"]

def test_get_sweets(sample_user):
    # Login first
    token = test_login_user(sample_user)
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/api/sweets", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_admin_create_sweet(admin_user):
    # Register admin
    client.post("/api/auth/register", json=admin_user)
    # Login admin
    login_res = client.post("/api/auth/login", data={"username": admin_user["username"], "password": admin_user["password"]})
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    new_sweet = {
        "name": "Test Candy",
        "category": "Test",
        "price": 1.99,
        "quantity": 100,
        "description": "Tasty",
        "image_url": "http://example.com/image.png"
    }
    
    response = client.post("/api/sweets", json=new_sweet, headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] == "Test Candy"

def test_search_sweets(sample_user):
    token = test_login_user(sample_user)
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/api/sweets/search?name=Test", headers=headers)
    assert response.status_code == 200
