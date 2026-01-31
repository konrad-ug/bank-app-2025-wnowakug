from src.mongo_accounts_repository import MongoAccountsRepository
from src.account import Account

class TestMongoRepo:

    def test_load_all_uses_collection(self, mocker):
        repo = MongoAccountsRepository()
        mock_collection = mocker.Mock()

        mock_collection.find.return_value = [
            {"first_name": "Jan", "last_name": "Kowalski", "pesel": "123", "balance": 100, "history": []}
        ]

        repo._collection = mock_collection

        accounts = repo.load_all()

        assert len(accounts) == 1
        assert accounts[0].first_name == "Jan"
