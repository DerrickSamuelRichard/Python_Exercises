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
            i -=1
        elif o.title() == 'Quit':
            print('Thank you for playing')
            break
        elif o.title() == 'Continue':
            m = str(input('do u want to remove(R) or add(A) it : '))
            if m.upper() == 'R' :
                n = int(input('enter a number : '))
                b = a.count(n)
                for j in range(0,b):
                    a.remove(n)
                print(a)
                print('done')
            elif m.upper() == 'A':
                p = int(input('enter a number : '))
                q= int(input('where do u want to add it : '))
                a.insert(q,p)
                print(a)
                print('done')
            else:
                i -=1
                print("WRONG INPUT".center(100,'-'))
        else:
            i -=1
                print("WRONG INPUT".center(100,'-'))    
    
    

















