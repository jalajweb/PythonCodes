print('Enter the items in the shoping list one by one.')
print("At last, type 'DONE' to Quit.")
print('\nEnter items:')

shoppingList = []
while True:
    item = input()
    shoppingList.append(item)
    if item == 'DONE':
        break
    
print('\nItems are:')
for i in range(len(shoppingList)-1):
    print(shoppingList[i])