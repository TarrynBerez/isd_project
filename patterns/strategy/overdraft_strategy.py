__author__ = "Tarryn Bereznycky"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class OverdraftStrategy(ServiceChargeStrategy):
    """
    Strategy for calculating service charges based on conditions.
    
    """
    
    def __init__(self, overdraft_limit : float, overdraft_rate : float):
        """
        Initializes the overdraft limit and overdraft rate for the strategy 
        
        Args:
            overdraft limit (float): The limit where overdraft charges apply.
            
            overdraft_rate (float): The rate used to calculate overdraft charges.
            
            """
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate
    
    
    def calculate_service_charges(self, account : BankAccount) -> float:
        """
        Calculates and returns the service charges.
        
        Args:
         bank_account (BankAccount): The bank account for which the service charges are calculated.
        
        Returns:
            float: The calculated service charge.
        
        """
        # Does account.balance work?
        if account.balance >= self.__overdraft_limit:
            value = self.BASE_SERVICE_CHARGE
        elif account.balance < self.__overdraft_limit:
            value = self.BASE_SERVICE_CHARGE + \
                (self.__overdraft_limit - account.balance) * self.__overdraft_rate
        return value