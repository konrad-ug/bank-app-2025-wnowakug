from src.account import Account


class TestAccount:
    def test_account_creation(self):
        account = Account("John", "Doe",9999,69093089679)
        assert account.first_name == "John", "nieprawidlowe imie"
        assert account.last_name == "Doe", "nieprawidlowe nazwisko"
        assert account.balance == 0, "niezerowy balans konta"
        assert account.pesel == 69093089679, "nieprawidłowy pesel"

    def test_pesel_length(self):
        account2 = Account("Jane","Doe",0,123)
        assert account2.pesel == "Invalid", "pesel jest zbyt krótki"
        account22 = Account("Jane", "doe",0,12345678900987654321)
        assert account22.pesel == "Invalid", "pesel jest zbyt długi"

    def test_code(self):
        account4 = Account("Jan", "Kowalski",0,90020223412,"PROM_ABC")
        assert account4.balance == 50, "Nie naliczono bonusu mimo poprawnego kodu"

    def test_wrong_code(self):
        account5 = Account("Marcin","Martychewicz",0,70031618343,"ABC_PROM")
        assert account5.balance == 0, "Naliczono bonus mimo błędnego kodu"

    def test_code_born_after_1960(self):
        account6 = Account("Jan", "Mlody", 0, 90010112345, "PROM_ABC")  # 1990
        assert account6.balance == 50, "nie naliczono bonusu mimo odpowiedniego wieku"
    
    def test_code_born_before_1960(self):
        account7 = Account("Jan", "Stary", 0, 60010112345, "PROM_ABC")  # 1960
        assert account7.balance == 0, "naliczono bonus mimo nieodpowiedniego wieku"


