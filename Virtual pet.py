class VirtualPet:
    def __init__(self,name):
        self.name = name
        self.size = 0
        self.age = 0
        self.energy = 25
        self.hungry = 5
        self.bored = 5
        self.foods = ["Pizza", "Ice Cream"]
        self.toys = ["Ball", "Frisbee"]
        print("I have been born")

    def play(self,toy):
        if toy in self.toys:
            if self.energy > 25:
                if toy == self.toys[0]:
                    self.bored = self.bored -3
                    self.energy = self.energy - 20
                    print("woof woof")
                elif toy == self.toys[1]:
                    self.bored = self.bored -2
                    print("woof")
                else:
                    print("I'm not playing")
            else:
                print("Not enough energy")


pet_one = VirtualPet("Jeff")

print("The pet is called {0}".format(pet_one.name ))

pet_one.play("Ball")
