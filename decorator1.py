class after5(object):
    def __init__(self, func):
        self.count = 0
        self.func = func

    def __call__(self):
        count = self.count

        if(count > 4):
            self.func()

        self.count = count + 1


@after5
def doit():
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
