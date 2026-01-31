import os
from pymongo import MongoClient
from src.account import Account
from src.company_account import C_Account


class MongoAccountsRepository:
    def __init__(self):
        mongo_url = os.getenv("BANK_APP_MONGO_URL", "mongodb://localhost:27017/")
        client = MongoClient(mongo_url)
        db = client["bank_app"]
        self._collection = db["accounts"]

    def save_all(self, accounts):
        self._collection.delete_many({})
        for account in accounts:
            self._collection.update_one(
                {"pesel": account.pesel},
                {"$set": account.to_dict()},
                upsert=True
            )

    def load_all(self):
        accounts = []
        for doc in self._collection.find():
            if doc.get("company_name"):
                acc = C_Account(doc["company_name"], doc["nip"], doc["balance"])
            else:
                acc = Account(doc["first_name"], doc["last_name"], doc["balance"], doc["pesel"])

            acc.history = doc.get("history", [])
            accounts.append(acc)

        return accounts
