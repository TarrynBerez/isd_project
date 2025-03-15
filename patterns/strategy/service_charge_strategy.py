__author__ = "Tarryn Bereznycky"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """
    Abstract class for implementing service charge calculation strategies.
    
    """
    BASE_SERVICE_CHARGE = 0.50   
    
    @abstractmethod
    def calculate_service_charges(self, account : BankAccount) -> float:
        """
        Calculates the service charges for a bank account.

        Args: 
            account (BankAccount): The bank account that service 
                charges will calculate.

        Returns:
            float: The calculated service charge for the account.
        
        """
        pass