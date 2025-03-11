__author__ = "Tarryn Bereznycky"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """
    Docstring!
    
    """
    BASE_SERVICE_CHARGE = 0.50   
    
    @abstractmethod
    def calculate_service_charges(self, account : BankAccount):
        """
        Docstring!
        
        """
        pass