__author__ = "Tarryn Bereznycky"
__version__ = "1.0.0"

from email_validator import validate_email, EmailNotValidError

class Client:
    """
    Docstring!

    """
    def __init__(self, client_number : int, first_name : str, last_name : str, email_address : str):
        #Client Number
        if isinstance(int,client_number):
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
            raise ValueError("Last name cannot be blank")

        #Email Address
        try:
            validate_email(email_address, check_deliverability = False)
        except:
            email_address = "email@pixell-river.com"
        self.__email_adress = email_address

    
    @property
    def client_number(self) -> int:
        """
        Docstring!

        """
        return self.__client_number
    
    @property
    def first_name(self) -> str:
        """
        Docstring!

        """
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        """
        Docstring!

        """
        return self.__last_name
    
    @property
    def email_address(self) -> str:
        """
        Docstring!

        """
        return self.__email_adress

    def __str__(self) -> str:
        """
        Docstring!

        """
        return f"{self.__last_name}, {self.__first_name} [{self.__client_number}] - {self.__email_adress}"