__author__ = "author name"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from datetime import date, timedelta 

class InvestmentAccount(BankAccount):
    """
    Docstring!

    """

    def __init__(self, account_number : int, client_number : int, 
                 balance : float, date_created : date, management_fee : float):
        """
        Docstring!

        """
        super().__init__(account_number, client_number, balance, date_created)

        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 356.25)

        try:
            self.__management_fee = float(management_fee)
        except ValueError:
            self.__management_fee = 2.55
        


    def get_service_charges(self):
        if self._date_created < self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + self.__management_fee
        


    def __str__(self):
        """
        Docstring!

        """
        if self._date_created < self.TEN_YEARS_AGO:
            return (f"Account_number: {self._BankAccount__account_number} Balance: ${self._BankAccount__balance:,.2f}\n"
                    f"Date Created: {self._date_created} Management Fee: ${self.__management_fee:,.2f} Account Type: Investment")
        else:
            return (f"Account_number: {self._BankAccount__account_number} Balance: ${self._BankAccount__balance:,.2f}\n"
                    f"Date Created: {self._date_created} Management Fee: Waived Account Type: Investment")

    
