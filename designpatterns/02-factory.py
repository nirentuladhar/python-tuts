class Dog:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof"

class Cat:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow"


def get_pet(pet="Dog"):
    # Factory method
    pets = dict(dog=Dog("Cocoa"), cat=Cat("Bro"))

    return pets[pet]

d = get_pet("cat")
print(d.speak())