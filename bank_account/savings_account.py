__author__ = "author name"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from datetime import date


class SavingsAccount(BankAccount):
    """
    SavingsAccount class: Maintains savings account data.
    
    """
     
    def __init__(self, account_number : int, client_number : int, 
                  balance : float, date_created : date, 
                  minimum_balance : float):
        """
        Initializes the SavingsAccount class with argument values.

        Args:
            account_number (int): Value representing account number.
            client_number (int): Value representing client number.
            balance (float): Value representing balance.
            date_created (date): Value representing the date the account was created.
            minimum_balance (float): The minum balance the savings account can have.

        Raises:
            ValueError: If account number is not numeric or client number
                is not numeric.

        """
        super().__init__(account_number, client_number, balance, date_created)
        
        #Minimum Balance
        try:
            self.__minimum_balance = float(minimum_balance)
        except ValueError:
            self.__minimum_balance = 50


        #Service Charge Premium
        self.SERVICE_CHARGE_PREMIUM = 2.00



    def get_service_charges(self) -> float:
        """
        Calculates the service charge of the transaction.

        Returns:
            float: The calculated service charge.
        
        """
        if self.balance >= self.__minimum_balance:
            value = self.BASE_SERVICE_CHARGE
        elif self.balance < self.__minimum_balance:
            value = self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM
        return value

    
    def __str__(self) -> str:
        """
        A formatted string represenation of the SavingsAccount class.

        Returns:
            str: String representation of the savings account.

        """
        return (f"{super().__str__()}\n"
                f"Minimum Balance: ${self.__minimum_balance:,.2f} Account Type: Savings")
    

