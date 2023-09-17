import pyperclip

charlist = ['1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s','d','f',
            'g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S',
            'D','F','G','H','J','K','L','Z','X','C','V','B','N','M',' ',',','.','!','"','£','$','%','^','&',
            '*',')','(','-','_','=','+','`','¬','¦','[',']','{','}','|',';',':',"'",'@','#','~','<','>','/','?']
listlen = int(len(charlist))
encryptOrDecrypt = (input('do you want to encrypt or decrypt (decrypt will take text from clipboard): '))
password = input('password: ')
if encryptOrDecrypt == 'encrypt' or 'e':
    textIn = input('what do you want to encrypt: ')
elif encryptOrDecrypt == 'decrypt' or 'd':
    textIn = pyperclip.paste()

lenthpass = int(len(password))
lenthin = int(len(textIn))
passwordIndex = 0
inputIndex = 0
final = ''
if encryptOrDecrypt == 'encrypt' or encryptOrDecrypt == 'e':
    for i in range(lenthin):
        changer = int(charlist.index(password[passwordIndex]))
        changed = changer + int(charlist.index(textIn[inputIndex]))
        if changed >= listlen:
            changed = changed - listlen + 1
        final = final + charlist[changed]
        passwordIndex = passwordIndex + 1
        inputIndex = inputIndex + 1
        if passwordIndex >= lenthpass :
            passwordIndex = 0

if encryptOrDecrypt == 'decrypt' or encryptOrDecrypt == 'd':
    for i in range(lenthin):
        changer = int(charlist.index(password[passwordIndex]))
        changed = int(charlist.index(textIn[inputIndex])) - changer
        if changed < 0:
            changed = changed + listlen - 1
        final = final + charlist[changed]
        passwordIndex = passwordIndex + 1
        inputIndex = inputIndex + 1
        if passwordIndex >= lenthpass :
            passwordIndex = 0
print(final)
pyperclip.copy(final)