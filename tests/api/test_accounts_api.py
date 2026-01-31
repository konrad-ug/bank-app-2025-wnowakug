import pytest
from app.api import app, registry
pytestmark = pytest.mark.api


@pytest.fixture(autouse=True)
def clear_registry():
   registry.accounts.clear()


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_create_account(client):
   response = client.post("/api/accounts", json={
      "name": "James",
      "surname": "Hetfield",
      "pesel": "89092909825"
   })

   assert response.status_code == 201, "Nie udało się utworzyć konta"


def test_get_all_accounts(client):
   client.post("/api/accounts", json={
      "name": "Lars",
      "surname": "Ulrich",
      "pesel": "75052612345"
   })

   response = client.get("/api/accounts")

   assert response.status_code == 200, "GET /api/accounts nie zwrócił statusu 200"
   assert isinstance(response.get_json(), list), "GET /api/accounts nie zwrócił listy kont"


def test_get_account_by_pesel(client):
   pesel = "12345678901"

   client.post("/api/accounts", json={
      "name": "A",
      "surname": "B",
      "pesel": pesel
   })

   response = client.get(f"/api/accounts/{pesel}")

   assert response.status_code == 200, "GET /api/accounts/<pesel> nie zwrócił 200"
   assert response.get_json()["pesel"] == pesel, "Zwrócony PESEL nie zgadza się z oczekiwanym"


def test_get_account_returns_404_when_not_found(client):
   response = client.get("/api/accounts/00000000000")

   assert response.status_code == 404, "API nie zwróciło 404 dla nieistniejącego konta"


def test_update_account(client):
   pesel = "22222222222"

   client.post("/api/accounts", json={
      "name": "Old",
      "surname": "Name",
      "pesel": pesel
   })

   response = client.patch(f"/api/accounts/{pesel}", json={"name": "New"})

   assert response.status_code == 200, "PATCH nie zwrócił 200 przy aktualizacji konta"

   check = client.get(f"/api/accounts/{pesel}")
   assert check.get_json()["name"] == "New", "Imię konta nie zostało zaktualizowane"


def test_delete_account(client):
   pesel = "33333333333"

   client.post("/api/accounts", json={
      "name": "X",
      "surname": "Y",
      "pesel": pesel
   })

   response = client.delete(f"/api/accounts/{pesel}")

   assert response.status_code == 200, "DELETE nie zwrócił 200 przy usuwaniu konta"

   check = client.get(f"/api/accounts/{pesel}")
   assert check.status_code == 404, "Konto nadal istnieje po usunięciu"

def test_create_account_with_duplicate_pesel_returns_409(client):
   payload = {
      "name": "Jan",
      "surname": "Kowalski",
      "pesel": "99999999999"
   }

   client.post("/api/accounts", json=payload)
   response = client.post("/api/accounts", json=payload)

   assert response.status_code == 409, "API nie zwróciło 409 dla duplikatu PESELu"

