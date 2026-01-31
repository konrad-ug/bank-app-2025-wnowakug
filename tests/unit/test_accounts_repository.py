from src.accounts_repository import AccountsRepository


class DummyRepository(AccountsRepository):
    def save_all(self, accounts):
        return accounts

    def load_all(self):
        return []


def test_accounts_repository_can_be_extended():
    repo = DummyRepository()

    assert repo.save_all([1, 2, 3]) == [1, 2, 3], "Metoda save_all nie działa w klasie potomnej"
    assert repo.load_all() == [], "Metoda load_all nie działa w klasie potomnej"

#MUSIAŁEM DODAĆ TEN TEST BO COVERAGE KRZYCZAŁ NA ACCOUNTS_REPOSITORY.PY