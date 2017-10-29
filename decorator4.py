"""fulfills Ynon Perek's nontrivial python, Decorator & Generators, part 4"""


class accepts(object):
    """Checks input values are the correct type"""
    def __init__(self, *args):
        """takes classes as input to check input in __call__ against"""
        self.classes = args

    def __call__(self, func):
        """throws AssertionError if input does not match classes"""

        def wrappedFunc(*args):
            for i in range(len(args)):
                errString = "Input argument: {} does not match ".format(i)
                errString = errString + "type: {}".format(self.classes[i])
                assert (isinstance(args[i], self.classes[i])), errString
            return func(*args)
        return wrappedFunc


# make sure function can only be called with a float and an int
@accepts(float, int)
def pow(base, exp):
    pass


def main():
    # raise AssertionError
    pow('x', 10)

if __name__ == '__main__':
    main()
