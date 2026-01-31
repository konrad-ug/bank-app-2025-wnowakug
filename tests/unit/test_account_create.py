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

    def test_promo_not_applied_when_pesel_invalid(self):
        acc = Account("A", "A", 0, 123, "PROM_ABC")
        assert acc.balance == 0


    def test_account_to_dict_returns_correct_structure(self):
        acc = Account("Jan", "Kowalski", 0, "90010112345")
        acc.przelew_przychodzacy(100)

        data = acc.to_dict()

        assert data["first_name"] == "Jan", "Niepoprawne first_name w to_dict()"
        assert data["last_name"] == "Kowalski", "Niepoprawne last_name w to_dict()"
        assert data["pesel"] == "90010112345", "Niepoprawny pesel w to_dict()"
        assert data["balance"] == 100, "Niepoprawne saldo w to_dict()"
        assert data["history"] == [100], "Niepoprawna historia w to_dict()"


