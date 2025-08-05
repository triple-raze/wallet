from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_main():
    # создание кошелька
    wallet = client.post("/api/v1/wallet/create").json()
    assert wallet is not None

    # получение кошелька
    uuid = wallet['uuid']
    assert client.get(f"/api/v1/wallet/{uuid}").status_code == 200

    # операция
    update = client.post(
        f"/api/v1/wallet/{uuid}/operation", 
        json={"operation_type": "DEPOSIT", "amount": 100}
    )
    assert update.status_code == 200
    assert update.json()['balance'] == 100
    
    # проверка значений кошелька
    client.post(
        f"/api/v1/wallet/{uuid}/operation", 
        json={"operation_type": "WITHDRAW", "amount": 50}
    )

    wallet = client.get(f"/api/v1/wallet/{uuid}").json()

    assert wallet['balance'] == 50

    # неправильный айди
    assert client.get("/api/v1/wallet/-Wrong-uuid-bruh").status_code == 404

    new_update = client.post(
        f"/api/v1/wallet/-Wrong-uuid-/operation",
        json={"operation_type": "DEPOSIT", "amount": 100500}
    )
    assert new_update.status_code == 404

    # отрциательные значения нельзя
    newer_update = client.post(
        f"/api/v1/wallet/{uuid}/operation",
        json={"operation_type": "DEPOSIT", "amount": -1337}
    )
    assert newer_update.status_code == 422

    

