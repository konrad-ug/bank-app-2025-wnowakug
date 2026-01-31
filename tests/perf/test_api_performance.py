import requests
import time

BASE = "http://127.0.0.1:5000"
BASE_URL = BASE + "/api/accounts"


def test_create_account_performance():
    requests.post(BASE + "/api/debug/full-reset")  # 🔥 pełny reset systemu

    start = time.time()
    response = requests.post(BASE_URL, json={
        "name": "Perf",
        "surname": "Test",
        "pesel": "90010112345"
    })
    duration = time.time() - start

    assert response.status_code == 201, "Nie udało się utworzyć konta"
    assert duration < 0.5, f"Tworzenie konta trwało za długo: {duration}s"


def test_incoming_transfers_performance():
    requests.post(BASE + "/api/debug/full-reset")  # 🔥 reset przed testem

    pesel = "88010112345"

    payload = {
        "name": "Transfer",
        "surname": "Perf",
        "pesel": pesel
    }

    create_resp = requests.post(BASE_URL, json=payload)
    assert create_resp.status_code == 201, "Nie udało się utworzyć konta do testu przelewów"

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

    response = requests.get(f"{BASE_URL}/{pesel}")
    assert response.status_code == 200, "Nie udało się pobrać konta po przelewach"
    assert response.json()["balance"] == 1000, "Saldo po 100 przelewach jest niepoprawne"


def test_delete_account_performance():
    requests.post(BASE + "/api/debug/full-reset")  # 🔥 reset przed testem

    pesel = "87010112345"

    requests.post(BASE_URL, json={
        "name": "Delete",
        "surname": "Perf",
        "pesel": pesel
    })

    start = time.time()
    response = requests.delete(f"{BASE_URL}/{pesel}")
    duration = time.time() - start

    assert response.status_code == 200, "Nie udało się usunąć konta"
    assert duration < 0.5, f"Usuwanie konta trwało za długo: {duration}s"
