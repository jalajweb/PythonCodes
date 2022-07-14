inp = input('Enter the elememt of list by space: ').split(' ')
list1 = []
list2 = []
for i in inp:
    list1.append(i)
for i in list1:
    if i == i[::-1]:
        #print('True')
        list2.append('true')
    else:
        #print('False')
        list2.append('false')
if 'true' in list2:
    print('True')
else:
    print('False')        