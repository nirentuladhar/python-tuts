#!/usr/bin/python3
def main():
    s = "String!"
    print(s)
    s = "This is a\nstring!"
    print(s)
    s = r"This is a\nstring!" #raw string
    print(s)

    n = 42
    s = "This is a {} string!".format(n)
    #format is an object of string object

    # \ removes first line
    s = """\
This is a string again
line after line
of more text
    """
    print(s)

if __name__ == "__main__":main()
