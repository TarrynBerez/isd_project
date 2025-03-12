__author__ = "Tarryn Bereznycky"
__version__ = "1.0.0"

from abc import abstractmethod
from patterns.observer.observer import Observer

class Subject:
    """
    Docstring!
    
    """

    def __init__(self):
        """
        Docstring!
        
        """
        self._observers = []
    

    @abstractmethod
    def attach(self, observer : Observer):
        pass


    @abstractmethod
    def detach(self, observer : Observer):
        pass


    @abstractmethod
    def notify(self, message : str):
        pass