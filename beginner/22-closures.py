def outer_func():
    message = "Hi"

    def inner_func():
        print(message) # free variable

    return inner_func

my_func = outer_func()

print(my_func)

my_func() #this is a closure

# closure is an inner function that remembers the variables created in its local scope
# even after its parent function has finished executed




# ------------------------------------------

def outer_func_2(msg):
    message = msg

    def inner_func():
        print(message) # free variable

    return inner_func

hi_func = outer_func_2("Hi")
hello_func = outer_func_2("Hello")

hi_func()
hello_func()