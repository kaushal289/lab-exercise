'''game finding a secret number within 3 attempts using while loop'''

num=3
guess=0
guess_limit=3
while guess<guess_limit:
    n = int(input('enter a number you like between 0 to 20:'))
    guess += 1
    if n==num:
        print('you are correct')
        break
else:
    print('Sorry, you failed.')


