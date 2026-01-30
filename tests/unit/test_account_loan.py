import pytest
from src.account import Account

@pytest.fixture
def account():
    return Account("Jan", "Kowalski", 0, 90010112345)

class TestLoan:
   def test_loan_rejected_less_than_5_transactions(self,account):
      #acc = Account("A", "A", 0, 90010112345)

      account.przelew_przychodzacy(100)
      account.przelew_przychodzacy(100)
      account.przelew_przychodzacy(100)

      assert account.submit_for_loan(50) is False

   def test_loan_rejected_when_last_three_not_incoming(self, account):
      #acc = Account("A", "A", 0, 90010112345)

      account.przelew_przychodzacy(100)
      account.przelew_przychodzacy(100)
      account.przelew_wychodzacy(account, 10) 
      account.przelew_przychodzacy(50)
      account.przelew_przychodzacy(20)

      assert account.submit_for_loan(50) is False

   def test_loan_rejected_when_sum_last_five_too_small(self, account):
      #acc = Account("A", "A", 0, 90010112345)

      for _ in range(5):
         account.przelew_przychodzacy(10)

      assert account.submit_for_loan(100) is False

   def test_loan_accepted(self, account):
      #acc = Account("A", "A", 0, 90010112345)

      account.przelew_przychodzacy(100)
      account.przelew_przychodzacy(50)
      account.przelew_przychodzacy(60)
      account.przelew_przychodzacy(40)
      account.przelew_przychodzacy(30)

      result = account.submit_for_loan(50)

      assert result is True
      assert account.balance == 330

   def test_loan_rejected_when_sum_equals_amount(self, account):
      #acc = Account("A", "A", 0, 90010112345)
      for _ in range(5):
         account.przelew_przychodzacy(10) 

      assert account.submit_for_loan(50) is False

   def test_loan_rejected_when_last_three_include_outgoing(self, account):
      #acc = Account("A", "A", 0, 90010112345)
      other = Account("B", "B", 0, 90010112345)

      account.przelew_przychodzacy(100)
      account.przelew_przychodzacy(100)
      account.przelew_wychodzacy(other, 10) 
      account.przelew_przychodzacy(50)
      account.przelew_przychodzacy(20)

      assert account.submit_for_loan(50) is False





