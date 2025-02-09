__author__ = "Tarryn Bereznycky"
__version__ = "1.0.0"

from datetime import date
from abc import ABC, abstractmethod

class BankAccount(ABC):
    """
    BankData class: Maintains BankAccount data.

    """
    #Base Service Charge
    
    def __init__(self, account_number : int, client_number : int, 
                 balance : float, date_created : date):
        """
        Initializes the class attribute with the argument values.

        Args:
            account_number (int): Value representing bank account number.
            client_number (int): Value representing client number.
            balance (float): value representing current account balance.

        Raises:
            ValueError: If account number is not numeric or client number
                is not numeric.

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

        #Date Created
        if isinstance(date_created ,date):
            self._date_created = date_created    
        else:
            self._date_created = date.today()
        
        #Base Service Charge
        self.BASE_SERVICE_CHARGE = 0.50

    
    @property
    def account_number(self) -> int:
        """
        Accessor for the account_number attribute.

        Returns:
            self.__account_number (int): value representing
                account_number.

        """
        return self.__account_number
    

    @property 
    def client_number(self) -> int:
        """
        Accessor for the client_number attribute.

        Returns:
            self.__client_number (int): Value representing
                the client number.

        """
        return self.__client_number
    

    @property
    def balance(self) -> float:
        """
        Accessor for the balance attribute.

        Returns:
            self.__balance (float): value representing the
                account balance.

        """
        return self.__balance
    


    def update_balance(self, amount : float):
        """
        Method that updates the current balance of the account.

        Args:
            amount (float): Value representing the updated balance.
        
        """
        try:
            self.__balance += float(amount)
        except ValueError:
            pass


    def deposit(self, amount : float):
        """
        Method that deposits money to account.

        Args:
            Amount: The amount of money that 
                deposits into balance.

        Raises: 
            ValueError: If deposit amount is 
                not numeric or is not positive.

        """
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"Deposit amount: "
                             f"{amount} must be numeric.")
            
        if amount <= 0:
            raise ValueError(f"Deposit amount: "
                             f"${amount:,.2f} must be positive.")
        
        self.update_balance(amount)
        
        
    def withdraw(self, amount : float):
        """
        Method that withdraws money from account balance.

        Args:
            amount (float): The amount of money to withdraw from
                balance.
            
        Raises:
            ValueError: If withdraw amount is negative, not numeric, 
                exeeds the balance.

        """
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"withdraw amount: {amount} "
                             f"must be numeric.")

        if amount <= 0: 
            raise ValueError(f"withdraw amount: ${amount:,.2f} "
                             f"must be positive.")
        elif amount > self.__balance:
            raise ValueError(f"Withdraw amount: ${amount:,.2f} must " 
                             f"not exceed the account balance: "
                             f"${self.__balance:,.2f}")
        
        self.update_balance(-amount)


    @abstractmethod
    def get_service_charges(self) -> float:
        pass
 
 
    def __str__(self) -> str:
        """
        Returns a string representatio of the account

        Returns:
            str: A formatted strong displaying the account number and balance
        """
        return (f"Account Number: {self.__account_number} "
                f"Balance: ${self.__balance:,.2f}")
    