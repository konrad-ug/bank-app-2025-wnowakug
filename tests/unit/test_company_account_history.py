from src.company_account import C_Account

class TestHistory:
   def test_company_history_for_outgoing_transfer(self):
      sender = C_Account("FirmaA", 1234567890, 0)
      receiver = C_Account("FirmaB", 1234567890, 0)

      sender.balance = 100
      sender.przelew_wychodzacy(receiver, 30)

      assert sender.history == [-30]
      assert receiver.history == [30]

   def test_company_history_for_incoming_transfer(self):
      acc = C_Account("FirmaA", 1234567890, 0)

      acc.przelew_przychodzacy(50)

      assert acc.history == [50]


   def test_history_for_express_transfer_company(self):
         sender = C_Account("FirmaA", 1234567890, 0)
         receiver = C_Account("FirmaB", 1234567890, 0)

         sender.balance = 100
         sender.przelew_wychodzacy_express(receiver, 20)

         assert sender.history == [-20, -5]
         assert receiver.history == [20]
