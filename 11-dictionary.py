
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
        pass
        # print(k, d[k])

    # alternate better way to define dictionaries
    x = dict(
        dup_one = 1,
        dup_two = 2,
        dup_three = 3,
        dup_four = 4,
        dup_five = "5"
    )

    combined_dict = dict(**d, **x)
    print(combined_dict)

    print('four' in x)
    print(d.get("three"))
    del d['four']
    d.pop('five')
    print(d)

if __name__ == "__main__": main()