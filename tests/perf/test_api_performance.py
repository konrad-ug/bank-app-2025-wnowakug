import requests
import time

BASE_URL = "http://127.0.0.1:5000/api/accounts"

def test_create_and_delete_account_performance():
    for i in range(100):
        pesel = f"990101{i:05d}"

        payload = {
            "name": "Perf",
            "surname": "Test",
            "pesel": pesel
        }

        start = time.time()
        response = requests.post(BASE_URL, json=payload, timeout=0.5)
        duration = time.time() - start

        assert response.status_code == 201, "Nie udało się utworzyć konta w teście performance"
        assert duration < 0.5, f"Tworzenie konta trwało za długo: {duration}s"

        start = time.time()
        response = requests.delete(f"{BASE_URL}/{pesel}", timeout=0.5)
        duration = time.time() - start

        assert response.status_code == 200, "Nie udało się usunąć konta w teście performance"
        assert duration < 0.5, f"Usuwanie konta trwało za długo: {duration}s"

def test_incoming_transfers_performance():
    pesel = "88010112345"

    payload = {
        "name": "Transfer",
        "surname": "Perf",
        "pesel": pesel
    }

    requests.post(BASE_URL, json=payload)

    for i in range(100):
        start = time.time()
        response = requests.post(
            f"{BASE_URL}/{pesel}/transfer",
            json={"amount": 10, "type": "incoming"},
            timeout=0.5
        )
        duration = time.time() - start

        assert response.status_code == 200, "Nie udało się zaksięgować przelewu przychodzącego"
        assert duration < 0.5, f"Księgowanie przelewu trwało za długo: {duration}s"

    # sprawdzenie salda
    response = requests.get(f"{BASE_URL}/{pesel}")
    assert response.json()["balance"] == 1000, "Saldo po 100 przelewach jest niepoprawne"

