#Game module

import GameProcess

(X,Y) = (0,1) #set up some module-wide constants

class Game(object):
    
    def __init__(self, num_players=2, board_size=(3,3) ):
        """Set up everything we need to run a game of tic-tac-toe."""
        self.game_specs = [num_players, board_size]
        self.magic_key = [8, 1, 6, 3, 5, 7, 4, 9, 2]
        self.master = [['1', -1, 0], ['2', -1, 0], ['3', -1, 0],\
                       ['4', -1, 0], ['5', -1, 0], ['6', -1, 0],\
                       ['7', -1, 0], ['8', -1, 0], ['9', -1, 0]]
        # [0] is for display, [1] is for locations taken, [2] is for locations

        self.game_won = False           # set to false until game is won
        self.game_winner = 'winner'     # sets who has won game
        self.turns = 0                  # Counts turns taken in current game
        self.player = ["X", "Y"]        # controls current and next player
        self.current = X                # sets the middle value in the self.master set, get rid of somehow?
        self.control = []               # only used for stalemate check, get rid of somehow?
        self.game_on = True             # set to true while game is still valid
        self.board_full = False         # set to false unless board is full
        
    def get_master(self):
        """Returns the array used to manage the game"""
        return self.master
    
    def get_gamestate(self):
        """returns true if game is ongoing, false if game is over"""
        return self.game_on
    
    def attempt(self, pin):
        """If new move isn't already taken this does all necessary operations to take it"""
        if (self.master[pin][1] > -1):
            return False
        else:
            self.master[pin][1] = self.current
            self.master[pin][0] = self.player[0]
            self.master[pin][2] = self.magic_key[pin] + self.current
            self.winning()
            if(self.game_winner == 'winner'):
                self.stale_check()
            self.take_move()
            return True
    
    def magic_test(self, a):
        """Tests the value of arithmetic to see if winning has happened"""
        if a == 15:
            self.game_winner = self.player[0]
            self.end_maint()
            return True
        elif a == 18:
            self.game_winner = self.player[0]
            self.end_maint()
            return True
        else:
            return False
    
    def winning(self):
        """Tests to see if winning combination exists"""
        if(self.master[0][2] != 0 and self.master[1][2] != 0 and self.master[2][2] != 0):
            a = self.master[0][2] + self.master[1][2] + self.master[2][2]
            self.magic_test(a)
        if(self.master[3][2] != 0 and self.master[4][2] != 0 and self.master[5][2] != 0):
            a = self.master[3][2] + self.master[4][2] + self.master[5][2]
            self.magic_test(a)
        if(self.master[6][2] != 0 and self.master[7][2] != 0 and self.master[8][2] != 0):
            a = self.master[6][2] + self.master[7][2] + self.master[8][2]
            self.magic_test(a)
        if(self.master[0][2] != 0 and self.master[4][2] != 0 and self.master[8][2] != 0):
            a = self.master[0][2] + self.master[4][2] + self.master[8][2]
            self.magic_test(a)
        if(self.master[2][2] != 0 and self.master[4][2] != 0 and self.master[6][2] != 0):
            a = self.master[2][2] + self.master[4][2] + self.master[6][2]
            self.magic_test(a)
        if(self.master[0][2] != 0 and self.master[3][2] != 0 and self.master[6][2] != 0):
            a = self.master[0][2] + self.master[3][2] + self.master[6][2]
            self.magic_test(a)
        if(self.master[1][2] != 0 and self.master[4][2] != 0 and self.master[7][2] != 0):
            a = self.master[1][2] + self.master[4][2] + self.master[7][2]
            self.magic_test(a)
        if(self.master[2][2] != 0 and self.master[5][2] !=0 and self.master[8][2] != 0):
            a = self.master[2][2] + self.master[5][2] + self.master[8][2]
            self.magic_test(a)

    
    def stale_check(self):
        """This checks to see if the game is over due to the board being full"""
        loop_control = 0
        self.control = []
        for a in self.master:
            self.control.append(self.master[loop_control][2])
            loop_control += 1
        if 0 not in self.control:
            self.game_on = False
            self.board_full = True
            self.quit_game()
    
    def take_move(self):
        """A player has attempted to make a move. What happens?"""
        self.turns += 1
        self.iterate_player()
    
    def iterate_player(self):
        """changes the player parameters, [0] is current, [1] is next"""
        if (self.player[0] == 'X'):
            self.player[0] = 'Y'
            self.player[1] = 'X'
            self.current = Y
        elif (self.player[0] == 'Y'):
            self.player[0] = 'X'
            self.player[1] = 'Y'
            self.current = X
    
    def end_maint(self):
        """This function performs all end of game cleanup"""
        self.game_won = True
        self.game_on = False
        
    def quote_wopr(self):
        """Waxes philosophical about 80s films, and military conquest"""
        if self.game_won == True:
            wopr_text = "Congratulations, {0},the game has been won, perhaps now\n" \
                        "we could play Global Thermonuclear Warfare?".format(self.game_winner)
            return wopr_text
        elif self.game_won == False:
            wopr_text = "That was futile, {0}, perhaps the only way to win is not to play?".format(self.player[0])
            return wopr_text
    
    def set_gameover(self):
        """Exits the game"""
        self.game_on = False
    
    def get_turns(self):
        """Returns the number of moves"""
        return self.turns
        
    def get_nextplayer(self):
        """Returns the next player"""
        return self.player[1]
        
    def is_won(self):
        """
        Tells if the game is won
        Input: none
        Returns: boolean
        """
        return self.game_won
    
    def who_won(self):
        """
        Tells who won the game
        Input: none
        Returns: string
        """
        return self.game_winner
