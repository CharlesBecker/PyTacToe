#Outputs module

import Menu
import GameBoard
import Errors

class Output(object):

    """
    Class: Output
    
    Handles all output as needed.  This will need to be changed to fit game environment.
    """
    
    def __init__(self):
        self.menu = Menu.Menu()
        self.board = GameBoard.GameBoard()
        self.gameErrors = Errors.Errors()
        
    def top_banner(self):
        """
        General welcome to the game
        Input: none
        Returns: void
        """
        print("Welcome to the new & MARVELOUSLY IMPROVED Tyc Tac Toe!");
        
    def print_board(self, master):
        """
        Prints the current board to the screen.
        Input: master(multi-dimensional array)
        Returns: void
        """
        self.board.pretty_print(master)
    
    def errors(self, type):
        """
        Prints an error to the screen
        Input: type(string) [indicates which error is detected]
        Returns: void
        """
        print("There was an error.")
        print(self.gameErrors.error_chooser(type))

    def main_prompt(self):
        """
        Doesn't print, but returns the general prompt used for input as a string.
        Returns: string
        """
        return "Enter a valid selection (or 'h' for help): "
    
    def end_thanks(self, number, gameState):
        """
        Prints a thanks for playing, along with info about the game
        Inputs: numer(int), gameState(boolean)
        Returns: void
        """
        if (gameState == False):
            state = "was not"
        else:
            state = "was"
        print("Thanks for playing!")
        print("The game " + str(state) + " won, with " + str(number) + " moves.")	
        
    def print_menu(self, selected):
        if (selected == 'main'):
            thisMenu = self.menu.main_menu()
            print("Ye Grande Olde Pythone Tyc-Tac-Toe Menue")
        for option in thisMenu:
            print("{0}".format(option))
            
    def general_output(self, message):
        print(message)
