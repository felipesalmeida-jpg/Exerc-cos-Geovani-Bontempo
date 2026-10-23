from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_raiz():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "API no ar"}


def test_somar():
    response = client.get("/somar/2/3")
    assert response.status_code == 200
    assert response.json() == {"resultado": 5}
