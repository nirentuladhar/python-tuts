def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

hi_func = outer_function("Yo")
hi_func()

# ----------------------------------------------

# decorators
# function that takes another function as an argument
# adds some kind of functionality
# returns another function

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("wrapper executed this before _{}_".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

# def display():
#     print("display function ran")
# decorated_display = decorator_function(display)
# decorated_display()

## ^^ THIS IS EQUIVALENT TO 
@decorator_function
def display():
    print("display function ran")
display()

@decorator_function
def display_info(name, age):
    print("display_info ran with args ({}, {})".format(name, age))
display_info("John", 25)


# -------------------------------------------
### THROUGH CLASSES
class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("CALL method executed this before _{}_".format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@decorator_class
def display():
    print("display function ran")
display()

@decorator_class
def display_info(name, age):
    print("display_info ran with args ({}, {})".format(name, age))
display_info("John", 25)