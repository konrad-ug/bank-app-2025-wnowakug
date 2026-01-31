from abc import ABC, abstractmethod

class AccountsRepository(ABC):

   @abstractmethod
   def save_all(self, accounts):
      pass # pragma: no cover

   @abstractmethod
   def load_all(self):
      pass # pragma: no cover
