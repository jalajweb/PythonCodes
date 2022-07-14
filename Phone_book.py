import re
file = open('simpsons_phone_book.txt','r')
for line in file:
    if re.search('^J[a-z]+\sNeu\s\d{3}-\d{4}',line):
        print(line)
file.close()