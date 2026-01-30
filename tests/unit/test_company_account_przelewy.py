from src.company_account import C_Account


class TestCompanyPrzelewy:
    def test_transfer_reduces_sender_and_increases_receiver_balance(self):
        sender = C_Account("FirmaA", 1234567890, 0)
        receiver = C_Account("FirmaB", 1234567890, 0)

        sender.balance = 100
        receiver.balance = 50

        sender.przelew_wychodzacy(receiver, 30)

        assert sender.balance == 70, "nie zabrano pieniędzy z konta firmowego wysyłającego przelew"
        assert receiver.balance == 80, "pieniądze nie dotarły na konto firmowe odbiorcy"

    def test_transfer_does_not_happen_when_insufficient_funds(self):
        sender = C_Account("FirmaA", 1234567890, 0)
        receiver = C_Account("FirmaB", 1234567890, 0)

        sender.balance = 20
        receiver.balance = 50

        sender.przelew_wychodzacy(receiver, 30)

        assert sender.balance == 20, "zabrano środki z konta firmowego mimo niewystarczającego balansu"
        assert receiver.balance == 50, "konto firmowe odbiorcy otrzymało przelew mimo braku środków u nadawcy"

    def test_company_transfer_to_self_is_blocked(self):
        acc = C_Account("FirmaA", 1234567890, 0)

        acc.balance = 100
        acc.przelew_wychodzacy(acc, 50)

        assert acc.balance == 100

