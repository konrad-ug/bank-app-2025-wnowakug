from src.account import Account


class TestAccount:
    def test_account_creation(self):
        account = Account("John", "Doe",0,69093089679,"PROM_ABC")
        assert account.first_name == "John", "nieprawidlowe imie"
        assert account.last_name == "Doe", "nieprawidlowe nazwisko"
        assert account.balance == 0, "niezerowy balans konta"
        assert account.pesel == 69093089679, "nieprawidłowy pesel"

    def test_pesel_length(self):
        account2 = Account("Jane","Doe",0,97698039096)
        assert len(str(account2.pesel)) == 11, "nieprawidlowa dlugosc peselu"

    def test_empty_code(self):
        account3 = Account("Wojtek", "Nowak", 0,12345678901)
        assert account3.balance ==0, "naliczono rabat mimo nie podania kodu"

    def test_wrong_code(self):
        account4 = Account("Franek","Czeczotka",50,11342547342,"test")
        assert not account4.promo_code.startswith("PROM_") and account4.balance == 50, "naliczono rabat mimo błędnego kodu"

    def test_no_ammount_added(self):
        account5 = Account("Marcin","Martychewicz",50,70031618343,"PROM_CDA")
        assert account5.promo_code.startswith("PROM_") and account5.balance != 0, "nie naliczono rabatu mimo poprawnego kodu"

