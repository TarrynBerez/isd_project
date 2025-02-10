__author__ = "author name"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from datetime import date, timedelta 

class InvestmentAccount(BankAccount):
    """
    InvestmentAccount class: Maintains investing account information.

    """

    def __init__(self, account_number : int, client_number : int, 
                 balance : float, date_created : date, management_fee : float):
        """
        Initializes the investment account class with argument values.

        account_number (int): Value representing account number.
        client_number (int): Value representing client number. 
        balance (float): value representing balance.
        date_created (date): The date the account was created.
        management_fee (float): Value representing management fee.

        """
        super().__init__(account_number, client_number, balance, date_created)

        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 356.25)

        try:
            self.__management_fee = float(management_fee)
        except ValueError:
            self.__management_fee = 2.55
        


    def get_service_charges(self):
        """
        Gets the service charge for the transaction.

        Returns:
            float: calculated service charge.
        
        """
        if self._date_created < self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + self.__management_fee
        


    def __str__(self):
        """
        Returns string representation of the investing account class.

        Returns:
            str: String representation of the investment account.

        """
        if self._date_created < self.TEN_YEARS_AGO:
            return (f"Account_number: {self._BankAccount__account_number} Balance: ${self._BankAccount__balance:,.2f}\n"
                    f"Date Created: {self._date_created} Management Fee: ${self.__management_fee:,.2f} Account Type: Investment")
        else:
            return (f"Account_number: {self._BankAccount__account_number} Balance: ${self._BankAccount__balance:,.2f}\n"
                    f"Date Created: {self._date_created} Management Fee: Waived Account Type: Investment")

    
