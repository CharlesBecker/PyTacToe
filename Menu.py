#Menu module

class Menu(object):
        
    def __init__(self, num = 1):
            pass
        
    def main_menu(self):
        """We need a menu!"""
        menu = ["b - reprint board", \
                "n - see who the next player is", \
                "m - count the moves taken so far", \
                "h - print this menu", \
                "t - see if someone is winning (the game does this on it's own)", \
                "v - varDump (for dev only)", \
                "x - quit game", \
                "s - save game", \
                "r - get raw board data (csv)", \
                "1-9 - try to take a move (ie. play!)"]
        return menu
