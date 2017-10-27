"""fulfills Ynon Perek's nontrivial python, Decorator & Generators, par1"""
class after5(object):
    """"""
    def __init__(self, func):
        """setc count and stores func as attribute"""
        self.count = 0
        self.func = func

    def __call__(self):
        """checks count, calls func if count < 4, count++"""
        count = self.count

        if(count > 4):
            self.func()

        self.count = count + 1


@after5
def doit():
    """prints 'Yo!'"""
    print("Yo!")


def main():
    # ignore the first 5 calls
    doit()
    doit()
    doit()
    doit()
    doit()

    # so only print yo once
    doit()

if __name__ == '__main__':
    main()
