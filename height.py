people = [{'name': 'Mary', 'height': 160},
                {'name': 'Isla', 'height': 80},
                {'name': 'Sam'}]
ht = [i['height'] for i in people if('height' in i)]
avg = sum(ht)/len(ht)
print(avg)
