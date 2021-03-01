from main import app
from starlette.testclient import TestClient

client = TestClient(app)
def test_get():
    response = client.get("/welcome")
    assert response.status_code == 200
    assert response.json() == {"Message": "Bonjour, ceci est la beta d'un algorithm d'analyse de sentiment", "Status Code": 200}


def test_invalide_token():
    response=client.post("/sentiment",
    json={"token" : "metal",
    "text": "super"})
    print("test invalide")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"Message" : "Token Invalide", "Status Code": 422}


def test_prediction():
    response=client.post("/sentiment",
    json={
        "token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        "text": "super"})
    print("test prediction")
    print(response.json())
    assert response.status_code == 422
    assert response.json() == {
            "text": "super", 
            "prediction": "positif"
    }