import sys

def main():
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
    #converts string to array of chars
    numbers = list(number)
    #converts each char to an integer
    numbers = list(map(int, numbers))
    return sum(numbers)

def checkIsNumber(value):
    if(value.lower()=='q'):
        return 0
    elif(value.isdigit()):
        print(sumNumbers(value))
        return 1
    else:
        print('That is not an integer or \'q\'.')
        return -1

def test():
    print('\nTesting...')
        

if __name__=="__main__":
    main()
