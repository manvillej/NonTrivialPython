"""fulfills Ynon Perek's nontrivial python, Decorator & Generators, part 3"""


def fibonacci(n):
    """ A generator for creating the Fibonacci numbers """
    a = 0
    b = 1
    counter = n
    placeholder = 1

    while(counter > 0):
        placeholder = a + b
        yield "fib({})".format(counter)
        a = b
        b = placeholder
        counter = counter - 1
    yield a
    return


def main():
    n = 10
    f = fibonacci(n)
    for x in f:
        print(x)


if __name__ == '__main__':
    main()
