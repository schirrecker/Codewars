MAXKEY = 20

def encrypt(text, key):
    encryptedText = ''
    for letter in text: 
        code = ord(letter)
        code += key
        newletter = chr(code)
        encryptedText += newletter
    return encryptedText

def decrypt(text, key):
    decryptedText = ''
    for letter in text: 
        code = ord(letter)
        code -= key
        newletter = chr(code)
        decryptedText += newletter
    return decryptedText

def decryptBrute(text): 
    for key in range(1, MAXKEY):
        print(decrypt(text, key))


code = (encrypt('',5))


decryptBrute(code)

'''
text = ""
for letter in text: 
    code = ord(letter)
    code += 1
    newletter = chr(code)
    print (newletter)

text2 = "OPO"
for letter in text2: 
    code = ord(letter)
    code -= 1
    newletter = chr(code)
    print (newletter)
'''

'''
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
##for letter in alphabet:
##    print (ord(letter))

for code in range(65, 90+1):
    print (chr(code))
'''

























