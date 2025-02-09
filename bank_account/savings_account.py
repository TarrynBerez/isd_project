__author__ = "author name"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from datetime import date


class SavingsAccount(BankAccount):
     
    def __init__(self, account_number : int, client_number : int, 
                  balance : float, date_created : date, 
                  minimum_balance : float):
        """
        Docstring!

        """
        super().__init__(account_number, client_number, balance, date_created)
        
        #Minimum Balance
        try:
            self.__minimum_balance = float(minimum_balance)
        except ValueError:
            self.__minimum_balance = 50

        #Service Charge Premium
        self.SERVICE_CHARGE_PREMIUM = 2.00



    def get_service_charges(self):
        if self.__balance >= self.__minimum_balance:
            return self.BASE_SERVICE_CHARGE
        elif self.__balance < self.__minimum_balance:
            self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM

    
    def __str__(self):
        return (f"Account Number: {self.__account_number} Balance: {self.__balance}\n"
                f"Minimum Balance: {self.__minimum_balance} Account Type: Savings")
    

