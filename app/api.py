from flask import Flask, request, jsonify
from src.account_registry import AccountRegistry
from src.account import Account

app = Flask(__name__)
registry = AccountRegistry()


@app.route("/api/accounts", methods=["POST"])
def create_account():
    data = request.get_json()

    account = Account(data["name"], data["surname"], 0, data["pesel"])
    registry.add_account(account)

    return jsonify({"message": "Account created"}), 201


@app.route("/api/accounts", methods=["GET"])
def get_all_accounts():
    accounts = registry.get_all_accounts()

    accounts_data = [
        {
            "name": acc.first_name,
            "surname": acc.last_name,
            "pesel": str(acc.pesel),
            "balance": acc.balance,
        }
        for acc in accounts
    ]

    return jsonify(accounts_data), 200


@app.route("/api/accounts/<pesel>", methods=["GET"])
def get_account_by_pesel(pesel):
   acc = registry.get_by_pesel(pesel)

   if acc is None:
      return jsonify({"error": "Account not found"}), 404

   return jsonify({
      "name": acc.first_name,
      "surname": acc.last_name,
      "pesel": str(acc.pesel),
      "balance": acc.balance
   }), 200

@app.route("/api/accounts/<pesel>", methods=["PATCH"])
def update_account(pesel):
   acc = registry.get_by_pesel(pesel)

   if acc is None:
      return jsonify({"error": "Account not found"}), 404

   data = request.get_json()

   if "name" in data:
      acc.first_name = data["name"]
   if "surname" in data:
      acc.last_name = data["surname"]

   return jsonify({"message": "Account updated"}), 200

@app.route("/api/accounts/<pesel>", methods=["DELETE"])
def delete_account(pesel):
   acc = registry.get_by_pesel(pesel)

   if acc is None:
      return jsonify({"error": "Account not found"}), 404

   registry.accounts.remove(acc)

   return jsonify({"message": "Account deleted"}), 200

