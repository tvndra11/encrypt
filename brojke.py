import pyperclip
import tkinter as tk
from tkinter import ttk
#imports

final=' '
encryptOrDecrypt = 'encrypt'

charlist = ['1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s','d','f',
            'g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S',
            'D','F','G','H','J','K','L','Z','X','C','V','B','N','M',' ',',','.','!','"','£','$','%','^','&',
            '*',')','(','-','_','=','+','`','¬','¦','[',']','{','}','|',';',':',"'",'@','#','~','<','>','/','?']
listlen = int(len(charlist))

def encrypt():
    truepass = password.get()
    textIn = entry.get()
    lenthpass = int(len(truepass))
    lenthin = int(len(textIn))
    passwordIndex = 0
    inputIndex = 0
    final = ''
    if encryptOrDecrypt == 'encrypt' or encryptOrDecrypt == 'e':
        for i in range(lenthin):
            changer = int(charlist.index(truepass[passwordIndex]))
            changed = changer + int(charlist.index(textIn[inputIndex]))
            if changed >= listlen:
                changed = changed - listlen + 1
            final = final + charlist[changed]
            passwordIndex = passwordIndex + 1
            inputIndex = inputIndex + 1
            if passwordIndex >= lenthpass :
                passwordIndex = 0
    output.config(text= final)
    return final

def Decrypt():
    truepass = password.get()
    textIn = entry.get()
    lenthpass = int(len(truepass))
    lenthin = int(len(textIn))
    passwordIndex = 0
    inputIndex = 0
    final = ''
    if encryptOrDecrypt == 'decrypt' or encryptOrDecrypt == 'd':
        for i in range(lenthin):
            changer = int(charlist.index(truepass[passwordIndex]))
            changed = int(charlist.index(textIn[inputIndex])) - changer
            if changed < 0:
                changed = changed + listlen - 1
            final = final + charlist[changed]
            passwordIndex = passwordIndex + 1
            inputIndex = inputIndex + 1
            if passwordIndex >= lenthpass :
                passwordIndex = 0
    output.config(text= final)
    return final


print(final)
pyperclip.copy(final)
final = final + '(copied to clipboard)'

window= tk.Tk()
window.title('cryptware')
title_lable = ttk.Label(master= window, text= 'encrypter or decrypter', font= 'roboto 31')
title_lable.pack()
frame = ttk.Frame(master = window)
frame.pack()
textIn = tk.StringVar()
password = tk.StringVar()
entry = ttk.Entry(master=frame, textvariable=textIn)
entry.pack()
textlabel = ttk.Label(font= 'roboto 14', text= 'text')
textlabel.pack()
buttonframe = ttk.Frame(master= window)
buttonframe.pack()
button1= ttk.Button(master= buttonframe, text= 'decrypt', padding= 2, command= Decrypt)
button1.pack(side= 'left')
button2 = ttk.Button(master= buttonframe, text= 'encrypt', padding= 2, command= encrypt)
button2.pack(side= 'left')
output = ttk.Label(master= window, font= 'roboto 20', text= final)
output.pack()
textIn = tk.StringVar()
passwordentry = ttk.Entry(show= '*', textvariable = password)
passwordentry.pack()
password = tk.StringVar()



window.mainloop()
