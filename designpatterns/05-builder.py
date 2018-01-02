# anti-pattern
# removes the complexity of building an object
# director, abstract builder (interfaces), concrete builder (implements the interfaces), product (object being built)
# doesn't rely on polymorphism
# uses divide and conquer strategy

class Director():
    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car

class Builder():
    # Abstract builder
    # creates a car object and keeps it as its attribute
    def __init__(self):
        self.car = None
    def create_new_car(self):
        self.car = Car()

class SkyLarkBuilder(Builder):
    # Concrete builder
    def add_model(self):
        self.car.model = "SkyLark"
    def add_tires(self):
        self.car.tires = "Regular tires"
    def add_engine(self):
        self.car.engine = "Turbo engine"

class Car():
    # Product
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return "{} | {} | {}".format(self.model, self.tires, self.engine)

builder = SkyLarkBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()

print(car)

