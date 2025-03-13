__author__ = "Tarryn Bereznycky"
__version__ = "1.0.0"

from email_validator import validate_email, EmailNotValidError
from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email
from datetime import date, datetime

class Client(Observer):
    """
    Client Class: Maintains Client data.

    """
    def __init__(self, client_number : int, first_name : str, 
                 last_name : str, email_address : str):
        """
        Initializes the class attribute with the agrument values.

        Args:
            client_number (int): A value representing the client 
                number.
            first_name (str): string containing the clients first name.
            last_name (str): string containing the clients last name.
            email_address (str): string containing email address.

        Raises:
            ValueError: if client_number isnt an int, first_name 
                or last_name is blank.
            EmailNotValidError:
                if email is not valid.
                
        """
        #Client Number
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be an int.")
        
        #First Name
        if len(first_name.strip()) > 0:
            self.__first_name = first_name
        else:
            raise ValueError("First name cannot be blank.")

        #Last Name
        if len(last_name.strip()) > 0:
            self.__last_name = last_name
        else:
            raise ValueError("Last name cannot be blank.")

        #Email Address
        try:
            validate_email(email_address, check_deliverability = False) 
        except EmailNotValidError:
            email_address = "email@pixell-river.com"
        self.__email_address = email_address

    

    @property
    def client_number(self) -> int:
        """
        Accessor for the client_number attribute.

        Returns:
            self.__client_number (int): Value 
                representing the client number.

        """
        return self.__client_number
    

    @property
    def first_name(self) -> str:
        """
        Accessor for first_name.

        Returns:
            self.__first_name (str): String containing 
                clients first name.

        """
        return self.__first_name
    

    @property
    def last_name(self) -> str:
        """
        Accessor for the last_name attribute.

        Returns:
            self.__last_name (str): String containing 
                clients last name.

        """
        return self.__last_name
    

    @property
    def email_address(self) -> str:
        """
        Accessor for the email_address attribute.

        Returns:
            self.__email_address (str): Str containing 
                clients email adress.

        """
        return self.__email_address
    

    def update(self, message : str):
        """
        Updates the observer with a notification message and sends an email.

        Args:
            message (str): The message content to be included in the email.
        
        """
        subject = f"ALERT: Unusual Activity: {date.today()}"
        message = f"Notification for {self.__client_number}: {self.__first_name} {self.__last_name}: {message}"

        simulate_send_email(self.__email_address, subject, message)



    def __str__(self) -> str:
        """
        A formatted string representation of the class 
            instance.

        """
        return (f"{self.__last_name}, {self.__first_name} "
                f"[{self.__client_number}] - {self.__email_address}")