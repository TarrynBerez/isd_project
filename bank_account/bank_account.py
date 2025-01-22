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
    



    def update_balance(self, amount : float) -> float:
        """
        Docstring!
        """
        try:
            self.__balance += float(amount)
            return self.__balance
        except ValueError:
            raise ValueError("Updated balance must be a float.")
        

    def deposit(self, amount):
        """
        Docstring!
        """
        if amount <= 0:
            raise ValueError(f"Deposit amount: {amount} must be positive")
        
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"Deposit amount: {amount} must be numeric")

        self.update_balance(amount)
        
        
    def withdrawal(self, amount):
        """
        Docstring!
        """
        if amount <= 0:
            raise ValueError(f"Withdawal amount: {amount} must be positive.")
        
        try:
            amount = float(amount)
        except:
            raise ValueError(f"Withdrawal amount: {amount} must be numeric.")
        
        self.update_balance(-amount)



        
    def __str__(self):
        """
        """
        return f"Account Number: {self.__account_number} Balance: ${self.__balance:,.2f}"