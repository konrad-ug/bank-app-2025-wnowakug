from src.company_account import C_Account


class TestPrzelewy:
    def test_express_transfer_company_account_takes_fee(self):
        sender = C_Account("FirmaA", 1234567890, 0)
        receiver = C_Account("FirmaB", 1234567890, 0)

        sender.balance = 100
        receiver.balance = 50

        sender.przelew_wychodzacy_express(receiver, 20)

        assert sender.balance == 75, "nie pobrano opłaty za przelew ekspresowy"
        assert receiver.balance == 70, "przelew ekspresowy nie dotarł do adresata"
    
    def test_express_transfer_company_can_go_minus_five(self):
        sender = C_Account("FirmaA", 1234567890, 0)
        receiver = C_Account("FirmaB", 1234567890, 0)

        sender.balance = 0

        sender.przelew_wychodzacy_express(receiver, 0)

        assert sender.balance == -5, "saldo konta nie obniżyło się do -5 po przelewie ekspresowym na kwotę całego balansu konta"

    def test_express_transfer_company_blocked_below_minus_five(self):
        sender = C_Account("FirmaA", 1234567890, 0)
        receiver = C_Account("FirmaB", 1234567890, 0)

        sender.balance = 0

        sender.przelew_wychodzacy_express(receiver, 10)

        assert sender.balance == 0
        assert receiver.balance == 0, "przelew dotarł do adresata mimo niewystarczającego balansu"

    def test_express_transfer_company_does_not_allow_extra_hidden_limit(self):
        sender = C_Account("FirmaA", 1234567890, 0)
        receiver = C_Account("FirmaB", 1234567890, 0)

        sender.balance = 1

        sender.przelew_wychodzacy_express(receiver, 1)

        assert sender.balance == 1
        assert receiver.balance == 0

    def test_express_transfer_uses_overdraft_limit(self):
        account = C_Account("FirmaB", 1234567890, 0)
        receiver = C_Account("FirmaA", 1234567890, 0)

        account.balance = 0
        account.przelew_wychodzacy_express(receiver, 0)

        assert account.balance == -5

    def test_company_transfer_blocked_when_insufficient_funds(self):
        sender = C_Account("FirmaA", 1234567890, 0)
        receiver = C_Account("FirmaB", 1234567890, 0)

        sender.balance = 10
        sender.przelew_wychodzacy(receiver, 50)

        assert sender.balance == 10
        assert receiver.balance == 0



    