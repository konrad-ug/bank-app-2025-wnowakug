from src.account import Account

class TestHistory:
   def test_history_for_outgoing_transfer(self):
      sender = Account("A", "A", 0, 90010112345)
      receiver = Account("B", "B", 0, 90010112345)

      sender.balance = 100

      sender.przelew_wychodzacy(receiver, 30)

      assert sender.history == [-30]
      assert receiver.history == [30]

   def test_history_for_incoming_transfer(self):
      acc = Account("A", "A", 0, 90010112345)

      acc.przelew_przychodzacy(50)

      assert acc.history == [50]

   def test_history_for_express_transfer_personal(self):
      sender = Account("A", "A", 0, 90010112345)
      receiver = Account("B", "B", 0, 90010112345)

      sender.balance = 100
      sender.przelew_wychodzacy_express(receiver, 20)

      assert sender.history == [-20, -1]
      assert receiver.history == [20]

