__author__ = "Tarryn Bereznycky"
__version__ = "1.0.0"

from abc import abstractmethod
from patterns.observer.observer import Observer

class Subject:
    """
    Maintains list of observers and notifies them of updates
    
    """

    def __init__(self):
        """
        Initializes the subject object with na empty list of observers 
        
        """
        self._observers = []
    

    @abstractmethod
    def attach(self, observer : Observer):
        """
        Adds an observer to the list of observers
        
        Args:
            observer (Observer): The observer object to be added from 
                the observer list

        """
        pass


    @abstractmethod
    def detach(self, observer : Observer):
        """
        Removes an observer from the list of observers
        
        Args:
            observer (Observer): The observer object to be removed from 
                the observer list
            
        """
        pass


    @abstractmethod
    def notify(self, message : str):
        """
        Notifies attached observers with a given message
        
        Args:
            message (str): The message to be sent to each observer
            
        """
        pass