# fibonacci series
a, b = 0, 1
while b < 50:
    print(b)
    a, b = b, a + b


fh = open("lines.txt")
for line in fh.readlines():
    # to remove linebreak end=""
    print(line, end="")