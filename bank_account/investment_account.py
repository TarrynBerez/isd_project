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

        Raises:
            ValueError: If account number is not numeric or client number
                is not numeric.

        """
        super().__init__(account_number, client_number, balance, date_created)

        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 356.25)

        try:
            self.__management_fee = float(management_fee)
        except ValueError:
            self.__management_fee = 2.55
        


    def get_service_charges(self) -> float:
        """
        Gets the service charge for the transaction.

        Returns:
            float: calculated service charge.
        
        """
        if self._date_created < self.TEN_YEARS_AGO:
            value = self.BASE_SERVICE_CHARGE
        else:
            value = self.BASE_SERVICE_CHARGE + self.__management_fee
        return value


    def __str__(self) -> str:
        """
        Returns string representation of the investing account class.

        Returns:
            str: String representation of the investment account.

        """
        if self._date_created < self.TEN_YEARS_AGO:
            fee = "Waived"
        else:
            fee = f"${self.__management_fee:,.2f}"
 
        return (f"{super().__str__()}\n"
                f"Date Created: {self._date_created} Management Fee: {fee} Account Type: Investment")


    
