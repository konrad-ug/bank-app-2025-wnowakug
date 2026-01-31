from src.company_account import C_Account
import pytest

class TestCompanyAccount:
    def test_company_account_creation(self):
        c_account1 = C_Account("Steam",1234567890,0)

        assert c_account1.company_name == "Steam", "Błędna nazwa firmy"
        assert c_account1.nip == 1234567890, "Błędny numer nip"

    def test_nip_length(self):

        c_account2 = C_Account("Nintendo",1231,0)

        assert c_account2.nip == "Invalid", "nieprawidłowa długość numeru nip"

    def test_constructor_raises_error_when_company_not_found(self, mocker):
        mocker.patch(
            "src.company_account.C_Account._check_nip_in_gov",
            return_value=False
        )

        with pytest.raises(ValueError, match="Company not registered!!"):
            C_Account("BadCompany", "1234567890", 0)

    def test_constructor_allows_valid_company(self, mocker):
        mocker.patch(
            "src.company_account.C_Account._check_nip_in_gov",
            return_value=True
        )

        acc = C_Account("GoodCompany", "8461627563", 0)

        assert acc.company_name == "GoodCompany", "Nie utworzono konta dla poprawnej firmy"

    def test_invalid_nip_length_does_not_call_gov_api(self, mocker):
        spy = mocker.patch(
            "src.company_account.C_Account._check_nip_in_gov"
        )

        C_Account("ShortNipCo", "1234", 0)

        spy.assert_not_called()


    def test_company_account_to_dict_returns_correct_structure(self):
        acc = C_Account("ACME", "1234567890", 0)
        acc.przelew_przychodzacy(500)
        acc.przelew_wychodzacy(acc, 0) 

        data = acc.to_dict()

        assert data["company_name"] == "ACME", "Niepoprawna nazwa firmy w to_dict()"
        assert data["nip"] == "1234567890", "Niepoprawny NIP w to_dict()"
        assert data["balance"] == 500, "Niepoprawne saldo w to_dict()"
        assert data["history"] == [500], "Niepoprawna historia w to_dict()"

    def test_check_nip_in_gov_returns_true_when_status_czynny(self, mocker):
        mock_response = mocker.Mock()
        mock_response.json.return_value = {
            "result": {
                "subject": {
                    "statusVat": "Czynny"
                }
            }
        }

        mocker.patch("src.company_account.requests.get", return_value=mock_response)

        acc = C_Account("ACME", "1234567890", 0)

        assert acc.nip == "1234567890", "NIP nie powinien być odrzucony gdy status VAT = Czynny"


    def test_check_nip_in_gov_returns_false_when_status_not_czynny(self, mocker):
        mock_response = mocker.Mock()
        mock_response.json.return_value = {
            "result": {
                "subject": {
                    "statusVat": "Zwolniony"
                }
            }
        }

        mocker.patch("src.company_account.requests.get", return_value=mock_response)

        with pytest.raises(ValueError, match="Company not registered"):
            C_Account("BadCorp", "1234567890", 0)
