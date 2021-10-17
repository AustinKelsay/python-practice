class PlayerCharacter:
    # Called constructor method or init method
    # The init method is called automatically when an object is instantiated
    # self is the placeholder name that refers to the object that will be instantiated
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

player1 = PlayerCharacter("Aus", 27)
player2 = PlayerCharacter("Jan", 25)
print(player1.name + " is " + str(player1.age))
print(player2.name + " is " + str(player2.age))

# You can assign totally new attributes to a specific object after it is created even though the class doesnt initially define it
player1.attack = 50
print(player1.attack)