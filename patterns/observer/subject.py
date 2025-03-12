__author__ = "Tarryn Bereznycky"
__version__ = "1.0.0"

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
    

    def attach(self, observer : Observer):
        pass


    def detach(observer : Observer):
        pass

 
    def notify(message : str):
        pass