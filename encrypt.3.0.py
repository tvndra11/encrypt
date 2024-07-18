import tkinter as tk
from tkinter import ttk
#imports

final='enter password below' #sets the output to enter password below to indicate to the user to use the bottom box
encryptOrDecrypt = 'encrypt'

charlist = ['1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s','d','f',#list of all the characters
            'g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S',
            'D','F','G','H','J','K','L','Z','X','C','V','B','N','M',' ',',','.','!','"','£','$','%','^','&',
            '*',')','(','-','_','=','+','`','¬','¦','[',']','{','}','|',';',':',"'",'@','#','~','<','>','/',
            '?','\n','×','\t','–','á','Á','à','À','ä','Ä','é','É','è','È','ê','Ê','ë','Ë','í','Í','Î','î','Ï',
            'ï','Ó','ó','ô','Ô','ú','Ú','Ö','ö','Û','û','Ü','ü','Ç','ç','“','”']
listlen = int(len(charlist))

def encrypt():
    truepass = passwordentry.get()#gets th pass word from the password box
    textIn = entry.get()#gets the text from the entry box
    lengthpass = int(len(truepass))
    lengthin = int(len(textIn))      #gets the length of the inputs
    passwordIndex = 0
    inputIndex = 0
    final = ''
    if 1 == 1:
        for i in range(lengthin):#repeat lengthin amount of times
            changer = int(charlist.index(truepass[passwordIndex]))#sets the changer to the place which letter number passwordIndex is in password is in charlist
            changed = changer + int(charlist.index(textIn[inputIndex]))#sets the changed to the changer plus the letter in the position of input index in charlist
            if changed >= listlen:
                changed = changed - listlen #if the changed number is longer than the list then wrap back round
            final = final + charlist[changed] #the output being built is the previous parts built plus the new part
            passwordIndex = passwordIndex + 1
            inputIndex = inputIndex + 1       #add to the indexs
            if passwordIndex >= lengthpass :
                passwordIndex = 0 #if the password index is longer than the actual password go back to the start of the password
    output.config(text= final)
    print(final)   #send the final to the console for checking if error occurs
    window.clipboard_clear()
    window.clipboard_append(final) #send to clipboard
    final = final + '(copied to clipboard)'
    return final #return the output

def Decrypt():
    truepass = passwordentry.get()
    textIn = entry.get()
    lengthpass = int(len(truepass))
    lengthin = int(len(textIn))
    passwordIndex = 0
    inputIndex = 0
    final = ''
    if 1 == 1:
        for i in range(lengthin):
            changer = int(charlist.index(truepass[passwordIndex]))
            changed = int(charlist.index(textIn[inputIndex])) - changer
            if changed < 0:
                changed = changed + listlen
            final = final + charlist[changed]
            passwordIndex = passwordIndex + 1
            inputIndex = inputIndex + 1
            if passwordIndex >= lengthpass :
                passwordIndex = 0
    output.config(text= final)
    print(final)
    window.clipboard_clear()
    window.clipboard_append(final)
    final = final + '(copied to clipboard)'
    return final

#                                 |
#things that make the window work |
#                                 V
window= tk.Tk()
window.title('cryptware')
title_lable = ttk.Label(master= window, text= 'encrypter or decrypter', font= 'roboto 31')
title_lable.pack()
frame = ttk.Frame(master = window)
frame.pack()
textIn = tk.StringVar()
truepass = tk.StringVar()
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
output = ttk.Label(master= window, font= 'Courier 20', wraplength=1800, text= final)
output.pack()
textIn = tk.StringVar()
passwordentry = ttk.Entry(show= '*', textvariable = truepass)
passwordentry.pack()
truepass = tk.StringVar()



window.mainloop() #boot up the window
