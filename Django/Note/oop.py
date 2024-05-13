class Human:
    def __init__(self, name): # Constructor
        self.name = name # Properties
        
    def say_hello(self): # method
        print(f'hello my name is {self.name}')

class Player(Human):
    def __init__(self, name, xp): # == constructor
        self.xp = xp

class Fan(Human):
    def __init__(self, name, fav_team):
        self.fav_team = fav_team

            
            
            
player = Player("d", 10)
player.say_hello()
player_fan = Fan("d_fan", "dont")
player_fan.say_hello()