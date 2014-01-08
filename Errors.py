# Errors module

class Errors(object):
    
    """
    Class: Errors
    
    Handles error messages
    """
    
    def __init__(self):
        pass
    
    def error_chooser(self, type):
        """Chooses appropriate error message to return"""
        if(type == "input"):
            return "Please enter a valid option."
        elif(type == "taken"):
            return "That space is taken, please choose another."
