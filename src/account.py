class Account:
    def __init__(self, first_name, last_name,balance,pesel,promo_code = None):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0
        self.pesel = pesel
        self.promo_code = promo_code
        self.history = []

        if len(str(self.pesel)) != 11:
            self.pesel = "Invalid"

        if self.promo_code is not None and self.promo_code.startswith("PROM_"):
            if self.rabat_wiek_check():
                self.balance += 50



    def rabat_wiek_check(self):
        if self.pesel == "Invalid":
            return False
        year = int(str(self.pesel)[0:2])
        full_year = 1900 + year
        return full_year > 1960
    
    def przelew_przychodzacy(self,kwota):
        self.balance += kwota
        self.history.append(kwota)

    def przelew_wychodzacy(self, cel, kwota):
        if cel is self:
            return

        if kwota <= self.balance:
            self.balance -= kwota
            self.history.append(-kwota)
            cel.przelew_przychodzacy(kwota)


    def przelew_wychodzacy_express(self, cel, kwota):
        fee = 1
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

    def submit_for_loan(self, amount):
        if len(self.history) < 5:
            return False

        last_three = self.history[-3:]
        if any(x <= 0 for x in last_three):
            return False

        if sum(self.history[-5:]) <= amount:
            return False

        self.balance += amount
        return True
