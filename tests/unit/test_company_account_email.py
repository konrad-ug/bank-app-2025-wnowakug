import pytest
from datetime import date
from src.company_account import C_Account

class TestCompanyAccountEmail:

    def test_send_history_email_company_success(self, mocker):
        mocker.patch("src.company_account.C_Account._check_nip_in_gov", return_value=True)

        acc = C_Account("Firma", "1234567890", 0)
        acc.history = [5000, -1000, 500]

        mock_send = mocker.patch("src.company_account.SMTPClient.send", return_value=True)

        result = acc.send_history_via_email("company@mail.com")

        assert result is True, "Metoda powinna zwrócić True dla poprawnej wysyłki maila"
        mock_send.assert_called_once()

        subject, text, email = mock_send.call_args[0]

        assert "Account Transfer History" in subject, "Temat maila firmowego nie zawiera nagłówka historii"
        assert str(date.today()) in subject, "Temat maila firmowego nie zawiera daty"
        assert "Company account history" in text, "Treść maila nie zawiera informacji o koncie firmowym"
        assert str(acc.history) in text, "Treść maila firmowego nie zawiera historii operacji"
        assert email == "company@mail.com", "Mail firmowy wysłano na zły adres"


    def test_send_history_email_company_failure(self, mocker):
        mocker.patch("src.company_account.C_Account._check_nip_in_gov", return_value=True)

        acc = C_Account("Firma", "1234567890", 0)
        acc.history = [1]

        mocker.patch("src.company_account.SMTPClient.send", return_value=False)

        result = acc.send_history_via_email("company@mail.com")

        assert result is False, "Metoda powinna zwrócić False gdy wysyłka maila firmowego się nie powiedzie"
