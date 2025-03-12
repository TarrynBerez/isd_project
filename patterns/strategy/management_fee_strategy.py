__author__ = "Tarryn Bereznycky"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount
from datetime import date, timedelta 

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Docstring!
    
    """
    def __init__(self, date_created : date, management_fee : float ):
        """
        Docstring
        
        """
        self.__date_created = date_created
        self.__management_fee = management_fee
        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)


    def calculate_service_charges(self, account : BankAccount) -> float:
        """
        Gets the service charge for the transaction.

        Returns:
            float: calculated service charge.
        
        """
        if self.__date_created < self.TEN_YEARS_AGO:
            value = self.BASE_SERVICE_CHARGE
        else:
            value = self.BASE_SERVICE_CHARGE + self.__management_fee
        return value