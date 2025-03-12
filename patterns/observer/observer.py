__author__ = "Tarryn Bereznycky"
__version__ = "1.0.0"

from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Docstring!
    
    """

    @abstractmethod
    def update(self, message : str):
        """
        Docstring!
        
        """
        pass