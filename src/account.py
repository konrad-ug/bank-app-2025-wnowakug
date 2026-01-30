class Account:
    def __init__(self, first_name, last_name,balance,pesel,promo_code = None):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0
        self.pesel = pesel
        self.promo_code = promo_code

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

    def przelew_wychodzacy(self, cel, kwota):
        if kwota <= self.balance:
            self.balance -= kwota
            cel.balance += kwota

    
    def przelew_przychodzacy_express(self,kwota):
        self.balance += kwota
    
    def przelew_wychodzacy_express(self, cel, kwota):
        fee = 1
        new_balance = self.balance - (kwota + fee)
        
        if new_balance >= 0:
            self.balance = new_balance
            cel.przelew_przychodzacy(kwota)
        elif self.balance == 0 and new_balance >= -fee:
            self.balance = new_balance
            cel.przelew_przychodzacy(kwota)