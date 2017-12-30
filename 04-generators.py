def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


# this is a generator
# what it does is it continues
# where it left off after "yielding"/returning a value
# to the place that called it
def primes(n = 1):
    while(True):
        if isprime(n): yield n
        n += 1

def print_primes():
    for n in primes():
        if n > 100: break
        print(n)

# ---------------------------------
    
def print_inclusive_range():
    for i in inclusive_range(25):
        print(i, end=" ")

def inclusive_range(*args):
    numargs = len(args)
    if numargs < 1: raise TypeError("requires at least 1 argument")
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError ("inclusive_range expected at most 3 arguments, got {}".format(numargs))

    i = start
    while i <= stop:
        yield i
        i += step



# ---------------------------------


def main():
    print_primes()
    print_inclusive_range()

if __name__ == "__main__": main()
