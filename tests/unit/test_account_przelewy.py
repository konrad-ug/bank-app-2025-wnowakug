from src.account import Account

@pytest.fixture
def sender():
    return Account("A", "A", 0, 90010112345)

@pytest.fixture
def receiver():
    return Account("B", "B", 0, 90010112345)

class TestPrzelewy:
    def test_transfer_reduces_sender_and_increases_receiver_balance(self,sender,receiver):
        sender.balance = 100  # ustawiamy stan początkowy
        receiver.balance = 50

        sender.przelew_wychodzacy(receiver, 30)

        assert sender.balance == 70, "nie zabrano pieniędzy z konta osoby wysyłającej przelew"
        assert receiver.balance == 80, "pieniądze nie dotarły na konto adresata przelewu"

    def test_transfer_does_not_happen_when_insufficient_funds(self,sender,receiver):
        sender.balance = 20
        receiver.balance = 50

        sender.przelew_wychodzacy(receiver, 30)

        assert sender.balance == 20, "zabrano środki z konta mimo niewystarczającego balansu"
        assert receiver.balance == 50, "otrzymano przelew mimo niewystarczającego balansu na koncie drugiej osoby"


    