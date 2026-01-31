import pytest
from datetime import date
from src.account import Account

class TestPersonalAccountEmail:

    def test_send_history_email_success(self, mocker):
        acc = Account("Jan", "Kowalski", 0, 90010112345)
        acc.history = [100, -1, 500]

        mock_send = mocker.patch("src.account.SMTPClient.send", return_value=True)

        result = acc.send_history_via_email("test@mail.com")

        assert result is True, "Metoda powinna zwrócić True gdy SMTP zwróci True"
        mock_send.assert_called_once()

        subject, text, email = mock_send.call_args[0]

        assert "Account Transfer History" in subject, "Temat maila nie zawiera nagłówka historii"
        assert str(date.today()) in subject, "Temat maila nie zawiera dzisiejszej daty"
        assert "Personal account history" in text, "Treść maila nie zawiera informacji o koncie osobistym"
        assert str(acc.history) in text, "Treść maila nie zawiera historii operacji"
        assert email == "test@mail.com", "Mail został wysłany na zły adres"


    def test_send_history_email_failure(self, mocker):
        acc = Account("Jan", "Kowalski", 0, 90010112345)
        acc.history = [100]

        mocker.patch("src.account.SMTPClient.send", return_value=False)

        result = acc.send_history_via_email("fail@mail.com")

        assert result is False, "Metoda powinna zwrócić False gdy SMTP zwróci False"
