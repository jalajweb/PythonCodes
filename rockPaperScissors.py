import random
print('Rock, Paper Scissors')
chances=['rock','paper','scissors']
while True:
    print('Select one choice either Rock, Paper or Scissors.\nIf correct, then you win otherwise computer wins.')
    uAction=input('your choice: ')
    cAction=random.choice(chances)
    print('computer choice: ',cAction)
    if uAction == cAction:
        print('both selected same, tie')
    elif uAction == 'rock' and cAction == 'scissors':
        print('you win')
    elif uAction == 'paper' and cAction == 'rock':
        print('wou win')
    elif uAction == 'scissors' and cAction == 'paper':
        print('you win')
    else:
        print('computer wins')
    print('Do you want to enter more (y/n): ')
    choice=input()
    if choice=='n' or choice=='N':
        break   