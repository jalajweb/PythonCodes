import random

fruits = ['apple', 'mango', 'banana', 'orange', 'grapes', 'watermelon', 'pineapple', 'kiwi', 'papaya', 'chikoo']
c_guess = random.choice(fruits)
u_guess = []
print('Choose any fruit name, if it is same as fruit choose by computer then you won, otherwise you loose.')
print('you have 5 chances to try.')
chance = 1
while chance <= 5:
    u_fruit = input('Enter the fruit: ').lower()
    u_guess.append(u_fruit)
    if u_fruit == c_guess:
        print('You won')
        break
    else:
        print('Try again!')
        chance = chance+1
    if chance == 5:
        print('you lost')