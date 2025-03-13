__author__ = "Tarryn Bereznycky"
__version__ = "1.0.0"

from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Abstract class for observers that receive notifications.
    
    """

    @abstractmethod
    def update(self, message : str):
        """
        Method to handle incoming notifications.

        Args:
            message (str): The notification message.
        
        """
        pass