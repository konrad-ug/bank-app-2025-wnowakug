import requests

BASE_URL = "http://127.0.0.1:5000/api/accounts"


def test_create_account():
    payload = {
        "name": "James",
        "surname": "Hetfield",
        "pesel": "89092909825"
    }

    response = requests.post(BASE_URL, json=payload)

    assert response.status_code == 201, "Nie udało się utworzyć konta"



def test_get_all_accounts():
   payload = {
      "name": "Lars",
      "surname": "Ulrich",
      "pesel": "75052612345"
   }

   requests.post(BASE_URL, json=payload)

   response = requests.get(BASE_URL)

   assert response.status_code == 200, "GET /api/accounts nie zwrócił statusu 200"
   assert isinstance(response.json(), list), "GET /api/accounts nie zwrócił listy kont"


def test_get_account_by_pesel():
   pesel = "12345678901"
   payload = {"name": "A", "surname": "B", "pesel": pesel}

   requests.post(BASE_URL, json=payload)

   response = requests.get(f"{BASE_URL}/{pesel}")


   assert response.status_code == 200, "GET /api/accounts/<pesel> nie zwrócił 200"
   assert response.json()["pesel"] == pesel, "Zwrócony PESEL nie zgadza się z oczekiwanym"

def test_get_account_returns_404_when_not_found():
   response = requests.get(f"{BASE_URL}/00000000000")

   assert response.status_code == 404, "API nie zwróciło 404 dla nieistniejącego konta"

def test_update_account():
   pesel = "22222222222"
   requests.post(BASE_URL, json={"name": "Old", "surname": "Name", "pesel": pesel})

   response = requests.patch(f"{BASE_URL}/{pesel}", json={"name": "New"})

   assert response.status_code == 200, "PATCH nie zwrócił 200 przy aktualizacji konta"

   check = requests.get(f"{BASE_URL}/{pesel}")
   assert check.json()["name"] == "New", "Imię konta nie zostało zaktualizowane"

def test_delete_account():
    pesel = "33333333333"
    requests.post(BASE_URL, json={"name": "X", "surname": "Y", "pesel": pesel})

    response = requests.delete(f"{BASE_URL}/{pesel}")

    assert response.status_code == 200, "DELETE nie zwrócił 200 przy usuwaniu konta"

    check = requests.get(f"{BASE_URL}/{pesel}")
    assert check.status_code == 404, "Konto nadal istnieje po usunięciu"



