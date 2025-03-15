# 10. Polymorphism with Functions
class Cat:
    def sound(self):
        return "Meow"

class Bird:
    def sound(self):
        return "Chirp"

def make_sound(animal):
    print(animal.sound())
