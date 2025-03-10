__author__ = "Tarryn Bereznycky"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """
    Docstring!
    
    """

    def __init__(self, overdraft_limit : float, overdraft_rate : float):
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate


    def get_service_charges(self) -> float:
        """
        Calculates and returns the service charges.

        Returns:
            float: The calculated service charge.

        """
        if self.balance >= self.__overdraft_limit:
            value = self.BASE_SERVICE_CHARGE
        elif self.balance < self.__overdraft_limit:
            value = self.BASE_SERVICE_CHARGE + \
                (self.__overdraft_limit - self.balance) * self.__overdraft_rate
        return value