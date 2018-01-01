def main():
    f = open("lines.txt")
    for index, line in enumerate(f.readlines()):
        print (index, line)

    s = "this is a string"
    for i, c in enumerate(s):
        if c == "s": print("index {} is an 's'".format(i))

if __name__=="__main__": main()