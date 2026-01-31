import os
import requests
from datetime import date
from smtp.smtp import SMTPClient

class C_Account:
    def __init__(self,company_name,nip,balance):
        self.company_name = company_name
        self.nip = nip
        self.balance = 0
        self.history=[]

        if len(str(self.nip)) != 10:
            self.nip = "Invalid"
            return

        if not self._check_nip_in_gov(self.nip):
            raise ValueError("Company not registered!!")

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

    def _has_required_balance(self, amount):
        return self.balance >= 2 * amount

    def _has_zus_payment(self):
        return -1775 in self.history
    
    def take_loan(self, amount):
        if not self._has_required_balance(amount):
            return False
        if not self._has_zus_payment():
            return False

        self.balance += amount
        return True
    
    def _check_nip_in_gov(self, nip):
        base_url = os.getenv("BANK_APP_MF_URL", "https://wl-test.mf.gov.pl/")
        today = date.today().isoformat()
        url = f"{base_url}api/search/nip/{nip}?date={today}"

        try:
            response = requests.get(url, timeout=2)
            data = response.json()
            print(data)

            return (
                data.get("result", {})
                    .get("subject", {})
                    .get("statusVat") == "Czynny"
            )

        except Exception:
            return True
        
    def send_history_via_email(self, email_address):
        subject = f"Account Transfer History {date.today()}"
        text = f"Company account history: {self.history}"

        return SMTPClient.send(subject, text, email_address)




