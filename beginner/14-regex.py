# pre compiled regex is more efficient

import re

def main():
    fh = open("raven.txt")
    for line in fh:
        if re.search("(Len|Neverm)ore", line):
            print(line, end="")

    print("--")

    fh = open("raven.txt")
    for line2 in fh:
        match = re.search("(Len|Neverm)ore", line2)
        if match: print(match.group())

    print("--")

    fh = open("raven.txt")
    for line in fh:
        match = re.search("(Len|Neverm)ore", line)
        if match:
            print(line.replace(match.group(), "###"), end="")

    print("--")

    fh = open("raven.txt")
    pattern = re.compile("(Len|Neverm)ore", re.IGNORECASE)
    for line in fh:
        if re.search(pattern, line):
            print(pattern.sub("###", line), end="")


if __name__ == "__main__": main()