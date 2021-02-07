from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..database import Base
from ..main import app, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///backend/tests/test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_valid_user():
    """Test create a valid user."""
    response = client.post(
        '/users/',
        json={'username': 'Enrique', 'password': '123'}
    )
    assert response.status_code == 200
    assert response.json() == {'username': 'Enrique', 'is_active': True, 'games': []}

def test_create_invalid_username_1():
    """Test create a user with an invalid username 1."""
    response = client.post(
        '/users/',
        json={'username': 'Enrique@', 'password': '123'}
    )
    assert response.status_code == 400

def test_create_invalid_username_2():
    """Test create a user with an invalid username 2."""
    response = client.post(
        '/users/',
        json={'username': '', 'password': '123'}
    )
    assert response.status_code == 400

def test_create_duplicated_username():
    """Test create a user with a duplicated username."""
    response = client.post(
        '/users/',
        json={'username': 'Enrique1', 'password': '123'}
    )
    assert response.status_code == 200
    assert response.json() == {'username': 'Enrique1', 'is_active': True, 'games': []}

    response = client.post(
        '/users/',
        json={'username': 'Enrique1', 'password': '123'}
    )
    assert response.status_code == 400

def test_create_missing_username():
    """Test create a user missing the username."""
    response = client.post(
        '/users/',
        json={'username': 'Enrique1', 'password': '123'}
    )
    assert response.status_code == 200
    assert response.json() == {'username': 'Enrique1', 'is_active': True, 'games': []}

def test_create_missing_username():
    """Test create a user missing the username."""
    response = client.post(
        '/users/',
        json={'password': '123'}
    )
    assert response.status_code == 422    

def test_create_missing_password():
    """Test create a user missing the password."""
    response = client.post(
        '/users/',
        json={'username': 'Enrique1'}
    )
    assert response.status_code == 422  

def test_read_valid_user():
    """Test read a valid user."""
    response = client.get(
        '/users/1',
    )
    assert response.status_code == 200
    assert response.json() == {'username': 'Enrique', 'is_active': True, 'games': []}

def test_read_invalid_user():
    """Test read a invalid user."""
    response = client.get(
        '/users/123',
    )
    assert response.status_code == 404
