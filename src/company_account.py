class C_Account:
    def __init__(self,company_name,nip,balance):
        self.company_name = company_name
        self.nip = nip
        self.balance = 0
        self.history=[]

        if len(str(self.nip)) != 10:
            self.nip = "Invalid"

    def przelew_przychodzacy(self,kwota):
        self.balance += kwota
        self.history.append(kwota)

    def przelew_wychodzacy(self, cel, kwota):
        if kwota <= self.balance:
            self.balance -= kwota
            self.history.append(-kwota)
            cel.przelew_przychodzacy(kwota)
    
    def przelew_wychodzacy_express(self, cel, kwota):
        fee = 5
        new_balance = self.balance - (kwota + fee)

        if new_balance >= 0:
            self.balance = new_balance
            self.history.append(-kwota)
            self.history.append(-fee)
            cel.przelew_przychodzacy(kwota)
        elif self.balance == 0 and new_balance >= -fee:
            self.balance = new_balance
            self.history.append(-kwota)
            self.history.append(-fee)
            cel.przelew_przychodzacy(kwota)



