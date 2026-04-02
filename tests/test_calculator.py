from app.calculator import multiply, sum, resta

def test_sum() -> None:
    assert sum(2, 3) == 5
    
def test_resta() -> None:
    assert resta(5, 3) == 2

def test_multiply() -> None:
    assert multiply(2, 3) == 6

# API tests
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_sum_endpoint():
    response = client.post("/sum", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 5}

def test_resta_endpoint():
    response = client.post("/resta", json={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_multiply_endpoint():
    response = client.post("/multiply", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 6}

