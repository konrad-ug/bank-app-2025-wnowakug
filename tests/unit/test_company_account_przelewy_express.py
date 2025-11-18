from src.company_account import C_Account


class TestPrzelewy:
    def test_money_not_recieved_express(self):
        account6 = C_Account("Sony",132547534,100)
        account7 = C_Account("Microsoft",6483740293,50)
        saldo = account7.balance

        kwota = 50

        account6.przelew_wychodzacy_express(account7,kwota)

        assert account7.balance == saldo+kwota, "pieniądze nie dotarły na konto"
    
    def test_not_enough_money(self):
        account6 = C_Account("Sony",132547534,100)
        account7 = C_Account("Microsoft",6483740293,50)
        
        kwota = 100

        assert account6.balance-kwota-1 >= -1, "niewystarczające środki na koncie"

        account6.przelew_wychodzacy_express(account7,kwota)

    def test_money_taken(self):
        account6 = C_Account("Sony",132547534,100)
        account7 = C_Account("Microsoft",6483740293,50)

        kwota = 50
        saldo = account6.balance

        account6.przelew_wychodzacy_express(account7,kwota)

        assert not account6.balance == saldo, "nie obciążono konta"
        assert not account6.balance == saldo-5, "pobrano opłatę za przelew ekspresowy, ale nie obciążono konta"
        assert not account6.balance == saldo-kwota, "konto zostało obciążone, ale nie pobrano opłaty za przelew ekspresowy"
        assert account6.balance == saldo-kwota-5, "konto zostało obciążone o złą ilość"
    