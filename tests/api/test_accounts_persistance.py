import requests
import pytest
pytestmark = pytest.mark.api

BASE = "http://127.0.0.1:5000"
BASE_URL = BASE + "/api/accounts"


def test_save_and_load_accounts():
    reset_resp = requests.post(BASE + "/api/debug/full-reset")
    assert reset_resp.status_code == 200, "Nie udało się zresetować stanu aplikacji"

    payload = {
        "name": "Save",
        "surname": "Test",
        "pesel": "99010112345"
    }

    create_resp = requests.post(BASE_URL, json=payload)
    assert create_resp.status_code == 201, "Nie udało się utworzyć konta"

    save_resp = requests.post(BASE_URL + "/save")
    assert save_resp.status_code == 200, "Nie udało się zapisać kont do bazy"

    delete_resp = requests.delete(BASE_URL + "/99010112345")
    assert delete_resp.status_code == 200, "Nie udało się usunąć konta z pamięci"

    load_resp = requests.post(BASE_URL + "/load")
    assert load_resp.status_code == 200, "Nie udało się wczytać kont z bazy"

    response = requests.get(BASE_URL + "/99010112345")
    assert response.status_code == 200, "Konto nie zostało odtworzone po wczytaniu z bazy"

    data = response.json()
    assert data["name"] == "Save", "Imię po odczycie z bazy jest niepoprawne"
    assert data["surname"] == "Test", "Nazwisko po odczycie z bazy jest niepoprawne"
    assert data["pesel"] == "99010112345", "PESEL po odczycie z bazy jest niepoprawny"
