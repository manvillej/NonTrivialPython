"""fulfills Ynon Perek's nontrivial python, Decorator & Generators, part 5"""


class returns(object):
    """Checks the return value is the correct type"""
    def __init__(self, returnClass):
        """takes class to check return value in __call__ against"""
        self.returnClass = returnClass

    def __call__(self, func):
        """throws AssertionError if input does not match classes"""

        def wrappedFunc(*args):
            results = func(*args)

            errString = "return value does not match type: "
            errString = errString + "{}".format(self.returnClass)

            assert (isinstance(results, self.returnClass)), errString
            return results

        return wrappedFunc


@returns(str)
def same(word):
    return word


def main():
    # works:
    same('hello')

    # raise AssertionError:
    same(10)

if __name__ == '__main__':
    main()
