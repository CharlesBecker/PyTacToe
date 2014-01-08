#Validation module

class Validation(object):
    
    """
    Class: Validation
    
    General validation to make sure that options are correct, deeper validation than 
    TextControl on it's own.
    """
    
    def __init__(self):
        pass
    
    def is_numeric(self, pin):
        """Tests if input is numeric"""
        temp = False
        try:
            int(pin)
            temp = True
        except:
            temp = False
        return temp
        
    def is_alpha(self, pin):
        """Tests if input is a letter"""
        temp = pin.isalpha()
        return temp
        
    def is_option(self, pin):
        """Tests if input is a valid menu option"""
        validOptions = "xbhnmtvsr?"
        if(pin in validOptions) and (pin != ''):
            return True
        else:
            return False
