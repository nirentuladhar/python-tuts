#!/usr/bin/python3

class Egg:
    # constructor
    def __init__(self, kind = "fried"):
        # object variable
        self.kind = kind

    # method
    def whatKind(self):
        return self.kind


def main():
    # object = encapsulation of methods and variables of the class
    fried = Egg()
    scrambled = Egg("scrambled")
    

if __name__ == "__main__":main()

# OBJECTS
# -----------------

# everything in python is an object incl. variables, functions, etc

# every object has an id, type and value
    # id uniquely idetifies particular instances of the object
        # cannot change for the life of the object
    # type identifies the class of an object
        # cannot change for the life of the object
    # value is the contents of the object
        # mutable objects can change value
        # immutable objects cannot


# VARIABLES
# -----------------

# all variables in python are first class objects
    # simple variable may be something more complex

# most fundamental types are IMMUTABLE
    # numbers, string, tuples

# mutable objects: lists, dictionary, etc
