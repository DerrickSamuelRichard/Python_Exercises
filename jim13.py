#!/usr/bin/python3
a = [5,6,7,8,9,5,5,5,5,2,3,4,4,56,6,]


for i in range(0,4):
    o = str(input('''
    OPTIONS:
    Help
    Continue
    Quit
    '''))
    print(a)
    i +=1
    if i == 3:
        print('this is your last chance')
    else:
        if o.title() == 'Help':
            print('''
            continue - continue the game
            quit - to quit the game
            you have three chances
            ''')
        elif o.title() == 'Quit':
            print('Thank you for playing')
            break
        else:
            m = str(input('do u want to remove(R) or add(A) it : '))