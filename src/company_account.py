class C_Account:
    def __init__(self,company_name,nip,balance):
        self.company_name = company_name
        self.nip = nip
        self.balance = balance

        if len(str(self.nip)) != 10:
            self.nip = "invalid"

    def przelew_przychodzacy(self,kwota):
        self.balance += kwota

    def przelew_wychodzacy(self,cel,kwota):
        if kwota <= self.balance:
            self.balance -= kwota
            cel.przelew_przychodzacy(kwota)
        else:
            pass
    
    def przelew_przychodzacy_express(self,kwota):
        self.balance += kwota

    def przelew_wychodzacy_express(self,cel,kwota):
        if kwota <= self.balance:
            self.balance -= kwota+5
            cel.przelew_przychodzacy(kwota)
        else:
            pass
    

