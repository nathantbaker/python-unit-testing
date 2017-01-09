from flight import *
from main import *
from running import *
from sidekick import *
from superhero import *
from swimming import *
from bulletproof import *

class Superman(Superhero, Flight, Running, Swimming, Bulletproof):

    def __init__(self):
        Superhero.__init__(self, "Superman")
        Bulletproof.__init__(self)
        self.air_speed = 1000000
        self.water_speed = 250