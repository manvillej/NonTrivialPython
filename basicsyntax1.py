running = True
while(running):
    value = input('Enter a number(press q to quit): ')
    if(value.lower()=='q'):
        running = False
    print(value)
