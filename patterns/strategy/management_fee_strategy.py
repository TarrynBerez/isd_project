__author__ = "Tarryn Bereznycky"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount
from datetime import date, timedelta 

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Strategy for calculating service charges based on 
    account creation date and management fee.
    
    """
    def __init__(self, date_created : date, management_fee : float ):
        """
        Initializes the ManagementFeeStrategy with the date 
        when the account was created and the management fee
        
        Args:
            date_created (date): The date the account was created
            
            management_fee(float): The management fee to be added 
                if the account was created within the last 10 years.
        """
        self.__date_created = date_created
        self.__management_fee = management_fee
        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)


    def calculate_service_charges(self, account : BankAccount) -> float:
        """
        Gets the service charge for the transaction.

        Args:
            account (BankAccount): The account where the services 
                charges are applied
        Returns:
            float: calculated service charge.
        
        """
        if self.__date_created < self.TEN_YEARS_AGO:
            value = self.BASE_SERVICE_CHARGE
        else:
            value = self.BASE_SERVICE_CHARGE + self.__management_fee
        return value