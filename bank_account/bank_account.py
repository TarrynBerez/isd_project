__author__ = "Tarryn Bereznycky"
__version__ = "1.0.0"

class BankAccount:
    """
    Docstring!
    """
    def __init__(self, account_number : int, client_number : int, balance : float):
        """
        Docstring!
        """
        #Account Number 
        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account number must be numeric.")
        
        #Client Number
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be numeric.")
        
        #Balance
        if isinstance(balance, float):
            self.__balance = balance
        else:
            raise ValueError("Balance must be a float type.")
        

    
    @property
    def account_number(self) -> int:
        """
        Docstring!
        """
        return self.__account_number
    

    @property 
    def client_number(self) -> int:
        """
        Docstring
        """
        return self.__client_number
    

    @property
    def balance(self) -> float:
        """
        Docstring!
        """
        return self.__balance
    
