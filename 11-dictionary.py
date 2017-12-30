
def main():
    d = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5
    }

    d['seven'] = 7
    # sorted alphabetically according to keys
    for k in sorted(d.keys()):
        print(k, d[k])

    # alternate better way to define dictionaries
    d = dict(
        one = 1,
        two = 2,
        three = 3,
        four = 4,
        five = "5"
    )

if __name__ == "__main__": main()