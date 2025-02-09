__author__ = "author name"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from datetime import date

class ChequingAccount(BankAccount):
    """
    Docstring

    """
    def __init__(self, account_number : int, client_number : int,
                 balance : float, date_created : date, overdraft_limit : float,
                 overdraft_rate : float):
        """
        Docstring!

        """
        
        super().__init__(account_number, client_number, balance,
                         date_created)
        
        #overdraft limit
        try:
            self.__overdraft_limit = float(overdraft_limit)
        except ValueError:
            self.__overdraft_limit = -100.00

        #overdraft rate 
        try:
            self.__overdraft_rate = float(overdraft_rate)
        except:
            self.__overdraft_rate = 0.05

    
    def get_service_charges(self):
        """
        Docstring

        """
        if self.__balance >= self.__overdraft_limit:
            return BankAccount.BASE_SERVICE_CHARGE
        elif self.__balance < self.__overdraft_limit:
            return BankAccount.BASE_SERVICE_CHARGE + (self.__overdraft_limit - self.__balance) * self.__overdraft_rate


    def __str__(self):
        """
        Docstring!

        """
        return (f"Account Number: {self.__account_number} Balance: {self.__balance}\n"
                f"Overdraft Limit: ${self.__overdraft_limit} Overdraft Rate: {self.__overdraft_rate}% Account Type: Chequing")