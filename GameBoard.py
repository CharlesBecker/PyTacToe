#TicTacToe module!

(X,Y) = (0,1) #set up some module-wide constants

class GameBoard(object):
        
    def pretty_print(self, master):
        """Returns a string representation of the board, suitable for printing to stdout"""
        line1 = '   |   |   '
        line2 = '---|---|---'
        print(line1)
        print(' {0[0][0]} | {0[1][0]} | {0[2][0]} '.format(master))
        print(line1)
        print(line2)
        print(line1)
        print(' {0[3][0]} | {0[4][0]} | {0[5][0]} '.format(master))
        print(line1)
        print(line2)
        print(line1)
        print(' {0[6][0]} | {0[7][0]} | {0[8][0]} '.format(master))
        print(line1)
