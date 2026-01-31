class AccountRegistry:

    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_by_pesel(self, pesel):
        for acc in self.accounts:
            if str(acc.pesel) == str(pesel):
                return acc
        return None


    def get_all_accounts(self):
        return self.accounts

    def count_accounts(self):
        return len(self.accounts)
    
    def pesel_exists(self, pesel):
        return any(str(acc.pesel) == str(pesel) for acc in self.accounts)

