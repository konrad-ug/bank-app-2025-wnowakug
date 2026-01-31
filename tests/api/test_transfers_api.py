import pytest
from app.api import app, registry

@pytest.fixture(autouse=True)
def clear_registry():
    registry.accounts.clear()

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_incoming_transfer_increases_balance(client):
   pesel = "90000000000"

   client.post("/api/accounts", json={
      "name": "A", "surname": "B", "pesel": pesel
   })

   response = client.post(f"/api/accounts/{pesel}/transfer", json={
      "amount": 100,
      "type": "incoming"
   })

   assert response.status_code == 200, "Incoming transfer nie zwrócił 200"
   
   acc = registry.get_by_pesel(pesel)
   assert acc.balance == 100, "Saldo nie zwiększyło się po przelewie przychodzącym"


def test_outgoing_transfer_decreases_balance(client):
   pesel = "90000000001"

   client.post("/api/accounts", json={
      "name": "A", "surname": "B", "pesel": pesel
   })

   registry.get_by_pesel(pesel).balance = 200

   response = client.post(f"/api/accounts/{pesel}/transfer", json={
      "amount": 50,
      "type": "outgoing"
   })

   assert response.status_code == 200, "Outgoing transfer nie zwrócił 200"
   assert registry.get_by_pesel(pesel).balance == 150, "Saldo nie zmniejszyło się poprawnie"


def test_outgoing_transfer_fails_when_no_funds(client):
   pesel = "90000000002"

   client.post("/api/accounts", json={
      "name": "A", "surname": "B", "pesel": pesel
   })

   response = client.post(f"/api/accounts/{pesel}/transfer", json={
      "amount": 50,
      "type": "outgoing"
   })

   assert response.status_code == 422, "API nie zwróciło 422 przy braku środków"


def test_express_transfer_takes_fee(client):
   pesel = "90000000003"

   client.post("/api/accounts", json={
      "name": "A", "surname": "B", "pesel": pesel
   })

   registry.get_by_pesel(pesel).balance = 100

   response = client.post(f"/api/accounts/{pesel}/transfer", json={
      "amount": 20,
      "type": "express"
   })

   assert response.status_code == 200, "Express transfer nie zwrócił 200"
   assert registry.get_by_pesel(pesel).balance == 79, "Nie pobrano opłaty 1 jednostki za express"


def test_transfer_returns_404_for_missing_account(client):
   response = client.post("/api/accounts/00000000000/transfer", json={
      "amount": 10,
      "type": "incoming"
   })

   assert response.status_code == 404, "API nie zwróciło 404 dla nieistniejącego konta"


def test_transfer_returns_400_for_invalid_type(client):
   pesel = "90000000004"

   client.post("/api/accounts", json={
      "name": "A", "surname": "B", "pesel": pesel
   })

   response = client.post(f"/api/accounts/{pesel}/transfer", json={
      "amount": 10,
      "type": "unknown"
   })

   assert response.status_code == 400, "API nie zwróciło 400 dla nieznanego typu przelewu"
