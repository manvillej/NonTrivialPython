"""Progam 1 of Ynon Perek's NonTrivial Python, asks the user for an integer, and returns the sum of the digits in that number"""
import sys

def main():
    """interprets the initial commandline argument to decide to run testing or the main program"""
    if(len(sys.argv)==1):
        running = True
        while(running):
            value = input('Enter a number(press q to quit): ')
            running = (checkIsNumber(value)!=0)
    elif(len(sys.argv)==2 and sys.argv[1] =='test'):
        test()
    else:
        print('\nWelcome to part 1 of NonTrivial Python: Basic Syntax')
        print('Run without arguments to access the main program')
        print('Run with the argument \'test\' to run the testing program\n')
            

def sumNumbers(number):
    """returns the sum of the individual numbers in number"""
    #converts string to array of chars
    numbers = list(number)
    #converts each char to an integer
    numbers = list(map(int, numbers))
    return sum(numbers)

def checkIsNumber(value):
    """returns 0 if value=q, 1 if value is digit, -1 otherwise"""
    if(value.lower()=='q'):
        return 0
    elif(value.isdigit()):
        print(sumNumbers(value))
        return 1
    else:
        print('That is not an integer or \'q\'.')
        return -1

def test():
    """runs a series of tests on the program"""
    print('\nTesting...')
        

if __name__=="__main__":
    main()
