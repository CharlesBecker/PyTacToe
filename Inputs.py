#Inputs module

class Inputs(object):
    
    def __init__(self):
        pass
    
    def get_keyboard(self, prompt):
    	self.tempIn = raw_input(prompt)
    	return self.tempIn
    
