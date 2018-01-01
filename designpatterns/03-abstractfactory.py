# the user expects multiple, related objects
# not known until runtime
class Dog:
    # one of the objects to be returned
    def speak(self):
        return "Woof"
    def __str__(self):
        return "Dog"

class DogFactory:
    # concrete factory
    def get_pet(self):
        # returns dog object
        return Dog()

    def get_food(self):
        # returns dog food object
        return "Dog Food!"

class PetStore:
    def __init__(self, pet_factory=None):
        # abstract factory
        self._pet_factory = pet_factory

    def show_pet(self):
        # utility method
        # displays details of objects returned by DogFactory
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is {}".format(pet))
        print("Our pet says hello by {}".format(pet.speak()))
        print("Its food is {}".format(pet_food))

# Concrete factory
factory = DogFactory()

# create a pet store housing the abstract factory
shop = PetStore(factory)

# utility method - show details
shop.show_pet()