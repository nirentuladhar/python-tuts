#!/usr/bin/python3
def main():
    x = (1,2,3) #tuple - immutable
    print(type(x), x)

    y = [4,5,6] #list - mutable
    y.append(5)
    y.insert(2, 7)
    print(type(y), y)

    z = "string"
    print(z[2])
    print(z[2:4]) #list slics #doesn't return last element

    a = range(1,5)
    # a = "string"
    for i in a: print(i)





if __name__ == "__main__":main()
