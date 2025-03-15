__author__ = "author name"
__version__ = "1.1.0"

from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy
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
            date_created (date): Value representing the date 
                the account was created.
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
    
        #Strategy
        self.__strategy = OverdraftStrategy(overdraft_limit, overdraft_rate)
    
    def get_service_charges(self) -> float:
        """
        Calculates and returns the service charges.

        Returns:
            float: The calculated service charge.

        """
        return self.__strategy.calculate_service_charges(self)
    
    
    def __str__(self) -> str:
        """
        A formatted string representation of the chequing account class

        Returns:
            str: formated string of chequing accound.

        """
        return (f"{super().__str__()}\n"
                f"Overdraft Limit: ${self.__overdraft_limit:,.2f} "
                f"Overdraft Rate: "
                f"{self.__overdraft_rate * 100:,.2f}% "
                f"Account Type: Chequing")