def main():
    # returns the list: ['baby', 'more', 'time']
    print("['baby', 'more', 'time']")
    print(longerThan(3, 'hit', 'me', 'baby', 'one', 'more', 'time'))


def longerThan(number, *args):
    """
    returns a list of all words longer than number.
    So much easier with list comprehension
    https://docs.python.org/3/tutorial/datastructures.html
    """
    results = [arg for arg in args if len(arg) > number]
    return results

if __name__ == '__main__':
    main()
