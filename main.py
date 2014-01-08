import Game
import Output
import Inputs
import TextControl

# instantiating objects
output = Output.Output()
game = Game.Game()
inputs = Inputs.Inputs()
textControl = TextControl.TextControl();

# Settings required for game play and initial output
errorInput = False
gameState = True
masterList = game.get_master()
output.top_banner()
output.print_menu("main")
mainPrompt = output.main_prompt()

# flow control and gameplay begins
while(gameState == True):
    output.print_board(masterList)
    if(errorInput != False):
        output.errors(errorInput)
    pin = inputs.get_keyboard(mainPrompt)
    if(textControl.is_valid_selection(pin)):
        if(textControl.is_valid_numeric(pin)):
            if(game.attempt(int(pin)-1) == False):
                errorInput = "taken"
            else:
                errorInput = False
        else:
            textControl.menu_option(pin, game, output)
            errorInput = False
    else:
        errorInput = "input"
    gameState = game.get_gamestate() 
    this = textControl.is_valid_selection(pin)
    if(gameState == False):
        if (game.is_won() == True):
            output.general_output(game.who_won() + " won!")
        else:
            output.general_output("No one won!")
        output.general_output("There were " + str(game.get_turns()) + " turns.")
        output.general_output(game.quote_wopr())
