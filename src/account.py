class Account:
    def __init__(self, first_name, last_name, balance, pesel,promo_code = None):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.pesel = pesel
        self.promo_code = promo_code

    def pesel_check(self):
        if len(str(self.pesel)) != 11:
            self.pesel = "invalid"

    def rabat_check(self):
        if self.promo_code != None and self.promo_code.startswith("PROM_"):
            self.balance += 50

    def rabat_wiek_check(self):
        p = str(self.pesel)

        if int(p[0]) >= 6 and int(p[2]) <= 1 or int(p[2]) >= 2:
            return True
        else:
            return False
