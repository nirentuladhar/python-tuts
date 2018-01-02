# restricts instantiation of a class to one object
# useful when exactly one object is need to coordinate actions across system
# considered to be anti-pattern
# because it introduces global state into an application
# BORG PATTERN, NOT EXACTLY A SINGLETON

class Borg:
    # makes class attributes global
    # oop form of global variable
    _shared_state = {} # attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_state

class Singleton(Borg):
    # Inherits from Borg class
    # This class will now share its attributes among all its instances
    def __init__(self, arg):
        # Update shared attribute dictionary
        Borg.__init__(self)
        self._shared_state = arg

    def __str__(self):
        return str(self._shared_state)

x = Singleton("Hyper Text Transfer Protocol")
print(x)

y = Singleton("Simple Mail Transfer Protocol")
print(y)

print(x)


