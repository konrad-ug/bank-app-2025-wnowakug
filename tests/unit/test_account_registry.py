import pytest
from src.account import Account
from src.account_registry import AccountRegistry

@pytest.fixture
def registry():
    return AccountRegistry()

@pytest.fixture
def sample_account():
    return Account("Jan", "Kowalski", 0, 90010112345)

class TestRegistry:
   def test_add_account(self,registry, sample_account):
      registry.add_account(sample_account)

      assert registry.count_accounts() == 1

   def test_find_account_by_pesel(self,registry, sample_account):
      registry.add_account(sample_account)

      found = registry.get_by_pesel(90010112345)

      assert found == sample_account

   def test_get_all_accounts(self,registry, sample_account):
      registry.add_account(sample_account)

      accounts = registry.get_all_accounts()

      assert len(accounts) == 1
      assert accounts[0] == sample_account

   def test_count_accounts(self,registry):
      acc1 = Account("A", "A", 0, 90010111111)
      acc2 = Account("B", "B", 0, 90010122222)

      registry.add_account(acc1)
      registry.add_account(acc2)

      assert registry.count_accounts() == 2
   
   def test_find_account_returns_none_when_not_found(self,registry):
      result = registry.get_by_pesel(123)

      assert result is None

   def test_registry_detects_duplicate_pesel(self):
      reg = AccountRegistry()
      acc = Account("A", "B", 0, "12345678901") 

      reg.add_account(acc)

      assert reg.pesel_exists("12345678901") is True, "Registry nie wykrył istniejącego PESELu"





