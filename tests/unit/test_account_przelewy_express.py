from src.account import Account


class TestPrzelewy:
    def test_money_not_recieved_express(self):
        account6 = Account("Natalia","Kaczmarska",100,12345678900)
        account7 = Account("Wojciech","Nowakowski",50,12309876543)
        saldo = account7.balance

        kwota = 50

        account6.przelew_wychodzacy_express(account7,kwota)

        assert account7.balance == saldo+kwota, "pieniądze nie dotarły na konto"
    
    def test_not_enough_money(self):
        account6 = Account("Natalia","Kaczmarska",100,12345678900)
        account7 = Account("Wojciech","Nowakowski",50,12309876543)
        
        kwota = 100

        assert account6.balance-kwota-1 >= -1, "niewystarczające środki na koncie"

        account6.przelew_wychodzacy_express(account7,kwota)

    def test_money_taken(self):
        account6 = Account("Natalia","Kaczmarska",100,12345678900)
        account7 = Account("Wojciech","Nowakowski",50,12309876543)

        kwota = 50
        saldo = account6.balance

        account6.przelew_wychodzacy_express(account7,kwota)

        assert not account6.balance == saldo, "nie obciążono konta"
        assert not account6.balance == saldo-1, "pobrano opłatę za przelew ekspresowy, ale nie obciążono konta"
        assert not account6.balance == saldo-kwota, "konto zostało obciążone, ale nie pobrano opłaty za przelew ekspresowy"
        assert account6.balance == saldo-kwota-1, "konto zostało obciążone o złą ilość"
    