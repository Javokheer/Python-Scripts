# This program says hello ans asks your name

def greater():
    print(' Hello world! ')
    print('What is your name?')                 # ask for their name
    name = input()
    print('It is going to meet you, ' + name)
    print('The lenth of your name is:'  )
    print(len(name))
    print('What is your age?')                      #ask for their age
    myAge = input()
    print('You will be ' + str(int(myAge)+1) + ' in a year. ')
    print(f'Great to meet you {name}, have a good week')

hello()

