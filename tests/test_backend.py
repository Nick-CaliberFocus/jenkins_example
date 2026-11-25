import pytest 
from fastapi.testclient import TestClient
from backend import app

client = TestClient(app)

def test_welcome():


    response = client.post("/")


    assert response.status_code == 200
    assert response.json() == {
        "message":"Arthimetic API is running"
    }

@pytest.mark.parametrize(
    "num1, num2, operation, expected",
    [
        (10, 20, "add", 30),
        (10, 5, "subtract", 5),
        (35, 5, "divide", 7),
        (3, 4, "multiply", 12),
        (45, 55, "add", 100),
        (0, 20, "multiply", 0)
    ]
)

def test_calculate(num1, num2, operation, expected):

    response = client.post(
        "/calculate",
        json={
            "num1": num1,
            "num2": num2,
            "operation": operation
        }
    )

    assert response.status_code == 200
    assert response.json()["result"] == expected

