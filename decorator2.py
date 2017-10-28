"""fulfills Ynon Perek's nontrivial python, Decorator & Generators, part 2"""


class memoize(object):
    """"""
    def __init__(self, func):
        """sets dictionary and stores func as attribute"""
        self.dictionary = {}
        self.func = func

    def __call__(self, n):
        """checks count, calls func if count < 4, count++"""
        if(n in self.dictionary.keys()):
            return self.dictionary[n]
        else:
            result = self.func(n)
            self.dictionary[n] = result
            return result


@memoize
def fib(n):
    """recursively calculates the fibonacci value of n"""
    print("fib({})".format(n))
    if(n <= 2):
        return 1
    else:
        return fib(n-1) + fib(n-2)


def main():
    print(fib(10))

if __name__ == '__main__':
    main()
