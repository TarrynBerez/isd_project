__author__ = "author name"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from datetime import date

class ChequingAccount(BankAccount):
    """
    ChequingAccount Class: Maintains savings account data.

    """
    def __init__(self, account_number : int, client_number : int,
                 balance : float, date_created : date, overdraft_limit : float,
                 overdraft_rate : float):
        """
        Initializes the Chequing account class with argument values.

        Args:
            account_number (int): Value representing account number.
            client_number (int): Value representing client number.
            balance (float): Value representing balance.
            date_created (date): Value representing the date the account was created.
            overdraft_limit (float): Value representing the overdraft limit.
            overdraft_rate (float): Value representing the overdraft limit.

        Raises:
            ValueError: If account number is not numeric or client number
                is not numeric.

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
        except ValueError:
            self.__overdraft_rate = 0.05

    
    def get_service_charges(self) -> float:
        """
        Calculates and returns the service charges.

        Returns:
            float: The calculated service charge.

        """
        if self.balance >= self.__overdraft_limit:
            value = self.BASE_SERVICE_CHARGE
        elif self.balance < self.__overdraft_limit:
            value = self.BASE_SERVICE_CHARGE + (self.__overdraft_limit - self.balance) * self.__overdraft_rate
        return value


    def __str__(self) -> str:
        """
        A formatted string representation of the chequing account class

        Returns:
            str: formated string of chequing accound.

        """
        return (f"{super().__str__()}\n"
                f"Overdraft Limit: ${self.__overdraft_limit:,.2f} Overdraft Rate: {self.__overdraft_rate * 100:,.2f}% Account Type: Chequing")