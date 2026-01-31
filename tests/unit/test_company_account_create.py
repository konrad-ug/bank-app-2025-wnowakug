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



