__author__ = "Tarryn Bereznycky"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Docstring!
    
    """
    def __init__(self, minimum_balance : float) -> float:
        self.SERVICE_CHARGE_PREMIUM = 2.0
        self.__minimum_balance = minimum_balance
        
        pass
    
    
    def calculate_service_charges(self, account : BankAccount) -> float:
        """
        Calculates the service charge of the transaction.
        
        Returns:
            float: The calculated service charge.
        
        """
        if account.balance >= self.__minimum_balance:
            value = self.BASE_SERVICE_CHARGE
        elif account.balance < self.__minimum_balance:
            value = self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM
        return value