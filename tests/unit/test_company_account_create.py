from src.company_account import C_Account

class TestCompanyAccount:
    def test_company_account_creation(self):
        c_account1 = C_Account("Steam",1234567890,0)

        assert c_account1.company_name == "Steam", "Błędna nazwa firmy"
        assert c_account1.nip == 1234567890, "Błędny numer nip"

    def test_nip_length(self):

        c_account2 = C_Account("Nintendo",9087654321,0)

        assert len(str(c_account2.nip)) == 10, "nieprawidłowa długość numeru nip"
