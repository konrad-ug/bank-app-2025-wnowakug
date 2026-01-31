import pytest
from src.account import Account

@pytest.fixture
def sender():
    return Account("A", "A", 0, 90010112345)

@pytest.fixture
def receiver():
    return Account("B", "B", 0, 90010112345)

class TestPrzelewy:
    def test_express_transfer_personal_account_takes_fee(self,sender,receiver):

        sender.balance = 100
        receiver.balance = 50

        sender.przelew_wychodzacy_express(receiver, 20)

        assert sender.balance == 79, "nie pobrano opłaty za przelew ekspresowy"
        assert receiver.balance == 70, "przelew ekspresowy nie dotarł do adresata"
    
    def test_express_transfer_personal_can_go_minus_one(self,sender,receiver):

        sender.balance = 0

        sender.przelew_wychodzacy_express(receiver, 0)

        assert sender.balance == -1, "saldo konta nie obniżyło się do -1 po przelewie ekspresowym na kwotę całego balansu konta"
    
    def test_express_transfer_personal_blocked_below_minus_one(self,sender,receiver):
        sender.balance = 0

        sender.przelew_wychodzacy_express(receiver, 5)

        assert sender.balance == 0
        assert receiver.balance == 0, "przelew dotarł do adresata mimo niewystarczającego balansu"

    def test_express_transfer_uses_overdraft_limit(self,sender,receiver):

        sender.balance = 0
        sender.przelew_wychodzacy_express(receiver, 0)

        assert sender.balance == -1




    