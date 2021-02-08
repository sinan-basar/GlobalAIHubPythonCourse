# HW5 - Homework

class Animals:
    def __init__(self, name, age, gender, color, tail_type):
        self.name        = name
        self.age         = age
        self.gender      = gender
        self.color       = color
        self.tail_type   = tail_type

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)

    def show_gender(self):
        print(self.gender)

    def show_color(self):
        print(self.color)

    def show_tail_type(self):
        print(self.tail_type)
        
    
class Dogs(Animals):
    def __init__(self):
        pass

    def call_dog(self):
        if self.gender == 'M':
            print("Handsome boy, come kuçu kuçu :D")
            self.woof()
        elif self.gender == 'F':
            print("Honey princess, come kuçu kuçu :D")
            self.woof()
        else:
            print("come kuçu kuçu :D")
            self.woof()
    
    def woof(self):
        print("Woof woof!")

    def play_ball(self):
        print("Let's play the ball!")

    def eat_something(self):
        print("Eating dog food!")

class Cats(Animals):
    def __init__(self):
        pass

    def call_cat(self):
        if self.gender == 'M':
            print("Handsome boy, come pisi pisi :D")
            self.meow()
        elif self.gender == 'F':
            print("Honey princess, come pisi pisi :D")
            self.meow()
        else:
            print("come pisi pisi :D")
            self.meow()
    
    def meow(self):
        print("Meow meow!")

    def play_ball_of_wool(self):
        print("Let's play the ball of wool!")

    def eat_something(self):
        print("Eating cat food!")

"""    
myDog = Dogs()

myDog.name = "Karabas"

myDog.gender = 'M'

myDog.show_name()
    
myDog.call_dog()
"""


myCats = Cats()

myCats.name = "Princess"

myCats.show_name()

myCats.gender = 'F'

myCats.show_gender()

myCats.call_cat()

myCats.eat_something()

myCats.play_ball_of_wool()

myCats.meow()
