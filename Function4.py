from collections import defaultdict


def main():
    """Runs groupby with example data"""

    # returns: { h: 1hello', 'hi', 'help', 'here'], b: ['bye'] }
    print("{'h': ['hello', 'hi', 'help', 'here'], 'b': ['bye']}")
    groupby(lambda s: s[0], 'hello', 'hi', 'help', 'bye', 'here')


def groupby(func, *args):
    """
    Creates dictionary with func(output) as the keys
    Inputs into function become a list of values for the key
    """

    oldDictionary = {arg: func(arg) for arg in args}

    resultDictionary = defaultdict(list)

    for key, value in oldDictionary.items():
        resultDictionary[value].append(key)

    # cast back into basic dict
    print(dict(resultDictionary))


if __name__ == '__main__':
    main()
