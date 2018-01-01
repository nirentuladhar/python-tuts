def main():
    testfunc(1,2,3,4,5,6,7,8)
    namedparameters(5,6,7,8,9,10, one = 1, two = 2, four = 42)


def testfunc(this, that, other, *args):
    # args is a tuple
    print(this, that, other, args)

# has to be in order though
def namedparameters(this, that, other, *args, **kwargs):
    # kwargs is a dictionary
    print("This is a test function", this, that, other, *args,
        kwargs["one"], kwargs["two"], kwargs["four"])


if __name__ == "__main__": main()
