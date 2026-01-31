import pytest
from src.company_account import C_Account

@pytest.fixture
def company_account():
    return C_Account("FirmaA", 1234567890, 0)

class TestLoan:

   @pytest.mark.parametrize("balance, loan_amount, expected", [
      (1000, 400, True), 
      (500, 400, False), 
   ])
   def test_company_loan_balance_condition(self,company_account, balance, loan_amount, expected):
      company_account.balance = balance
      company_account.history.append(-1775) 

      result = company_account.take_loan(loan_amount)

      assert result is expected
   

   @pytest.mark.parametrize("history, expected", [
      ([-1775], True),
      ([-100, -200], False),
   ])
   def test_company_loan_requires_zus_payment(self,company_account, history, expected):
      company_account.balance = 1000
      company_account.history = history

      result = company_account.take_loan(300)

      assert result is expected

   def test_company_loan_adds_balance_when_approved(self,company_account):
      company_account.balance = 1000
      company_account.history = [-1775]

      result = company_account.take_loan(300)

      assert result is True
      assert company_account.balance == 1300

   def test_company_loan_does_not_change_balance_when_rejected(self,company_account):
      company_account.balance = 200
      company_account.history = []

      result = company_account.take_loan(300)

      assert result is False
      assert company_account.balance == 200


