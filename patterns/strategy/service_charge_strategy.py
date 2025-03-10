__author__ = "Tarryn Bereznycky"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """
    Docstring!
    
    """
    @abstractmethod
    def calculate_service_charge(self, account : BankAccount):
        """
        Docstring!

        """
        self.BASE_SERVICE_CHARGE = 0.50
        pass