import random

x = random.randint(0,10)
y = int(input('Guess the number in range of 1-10: '))

if x == y:
    print('player wins and computer loss')
else:
    print('player loss and computer wins')