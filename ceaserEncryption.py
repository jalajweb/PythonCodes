def encryption(text,key):
    result=""
    for i in range(len(text)):
        ch = text[i]
        if ch.isupper():
            result = result+chr((ord(ch)+key-65)%26+65)
        else:
            result = result+chr((ord(ch)+key-97)%26+97)
    return result

def decryption(text,key):
    result=""
    for i in range(len(text)):
        ch = text[i]
        if ch.isupper():
            result = result+chr((ord(ch)-key-65)%26+65)
        else:
            result = result+chr((ord(ch)-key-97)%26+97)
    return result

print('example of ceaser encryption and decryption:\n')
plaintext = input('enter plain text: ')
ekey = int(input('enter key: '))
print('cypher text: '+encryption(plaintext,ekey))
cyphertext = encryption(plaintext,ekey)
print('plain text after decryption: '+decryption(cyphertext,ekey))