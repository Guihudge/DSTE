from random import randint

class Qbit:
    polarisation:int
    value:int
    FirstReadValue:int = None

    def __init__(self, polarisation, value):
        self.polarisation = polarisation
        self.value = value
    
    def read(self, polarisation):
        if(self.FirstReadValue != None):
                return self.FirstReadValue
        else: 
            if(polarisation == self.polarisation):
                return self.value
            else:
                val = randint(0,1)
                self.FirstReadValue = val
                return val