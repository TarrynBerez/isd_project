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
        try:
            balance = float(balance)
            self.__balance = balance
        except ValueError:
            self.__balance = 0
        

    
    @property
    def account_number(self) -> int:
        """
        Docstring!

        """
        return self.__account_number
    

    @property 
    def client_number(self) -> int:
        """
        Docstring!

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
            #return self.__balance
        except ValueError:
            pass
            # self.__balance = self.__balance
            # return self.__balance
            #raise ValueError("Updated balance must be a float.")
        

    def deposit(self, amount : float):
        """
        Docstring!

        """
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"Deposit amount: {amount} must be numeric")
            
        if amount <= 0:
            raise ValueError(f"Deposit amount: {amount:,.2f} must be positive")
        
        self.update_balance(amount)
        
        
    def withdraw(self, amount : float):
        """
        Docstring!

        """
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"withdraw amount: {amount} must be numeric.")

        if amount <= 0: 
            raise ValueError(f"withdraw amount: ${amount:,.2f} must be positive.")
        elif amount > self.__balance:
            raise ValueError(f"Withdraw amount: ${amount:,.2f} must not exeed the account balance: {self.__balance:,.2f}")
        
        self.update_balance(-amount)


    def __str__(self):
        """
        Docstring!
        
        """
        return f"Account Number: {self.__account_number} Balance: ${self.__balance:,.2f}"