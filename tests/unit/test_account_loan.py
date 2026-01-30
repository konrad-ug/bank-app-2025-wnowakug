from src.account import Account


class TestLoan:
   def test_loan_rejected_less_than_5_transactions(self):
      acc = Account("A", "A", 0, 90010112345)

      acc.przelew_przychodzacy(100)
      acc.przelew_przychodzacy(100)
      acc.przelew_przychodzacy(100)

      assert acc.submit_for_loan(50) is False

   def test_loan_rejected_when_last_three_not_incoming(self):
      acc = Account("A", "A", 0, 90010112345)

      acc.przelew_przychodzacy(100)
      acc.przelew_przychodzacy(100)
      acc.przelew_wychodzacy(acc, 10) 
      acc.przelew_przychodzacy(50)
      acc.przelew_przychodzacy(20)

      assert acc.submit_for_loan(50) is False

   def test_loan_rejected_when_sum_last_five_too_small(self):
      acc = Account("A", "A", 0, 90010112345)

      for _ in range(5):
         acc.przelew_przychodzacy(10)

      assert acc.submit_for_loan(100) is False

   def test_loan_accepted(self):
      acc = Account("A", "A", 0, 90010112345)

      acc.przelew_przychodzacy(100)
      acc.przelew_przychodzacy(50)
      acc.przelew_przychodzacy(60)
      acc.przelew_przychodzacy(40)
      acc.przelew_przychodzacy(30)

      result = acc.submit_for_loan(50)

      assert result is True
      assert acc.balance == 330

   def test_loan_rejected_when_sum_equals_amount(self):
      acc = Account("A", "A", 0, 90010112345)
      for _ in range(5):
         acc.przelew_przychodzacy(10) 

      assert acc.submit_for_loan(50) is False




