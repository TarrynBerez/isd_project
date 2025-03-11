from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
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


    def get_service_charges(self) -> float:
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