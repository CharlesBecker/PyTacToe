# TextControl module

import Validation

class TextControl(object):
    """
    Class: TextControl
    
    Specific controls for text based game play
    This module will have to be created uniquely or extended depending on gameplay
    environment.
    """
    
    def __init__(self):
        self.validater = Validation.Validation()
        
    def is_valid_numeric(self, pin):
        """Tests to see if the number is a valid option"""
        if(self.validater.is_numeric(pin)):
            pin = int(pin)
            if(pin != 0 and pin <= 9):
                return True
            else:
                return False
        else:
            return False
 
    def is_valid_selection(self, pin):
        """Tests to see if the user input (pin) is a valid selection"""
        if(self.validater.is_numeric(pin)):
            return True
        elif(self.validater.is_alpha(pin)):
            return self.validater.is_option(pin.lower())
        else:
            return self.validater.is_option(pin)
 
    def menu_option(self, pin, game, output):
        """Chooses what action to perform based on option"""
        if(pin == "x"):
            game.set_gameover();
            output.end_thanks(game.get_turns(), game.get_gamestate()) 
        elif(pin == "?") or (pin =="h"):
            output.print_menu("main")
        elif(pin == "b"):
            output.print_board(game.get_master())
        elif(pin == "n"):
            next = game.get_nextplayer()
            output.general_output("The next player is " + next + ".")
        elif(pin == "m"):
            turns = game.get_turns()
            output.general_output("There have been " + str(turns) + " turns so far.")
        else:
            output.general_output("This functionality is not available currrently.")  
                 
