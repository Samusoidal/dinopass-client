import requests, os
from tkinter import *

'''
Creates the GUI Frame with a gray background and a title.
'''
root = Tk()
root.configure(background="gray")
root.title("DinoPass Client")

'''
Initialises the password and password type.
'''
password = StringVar() #Password
ptype = StringVar() #Password type

'''
Adds a label and packs it into the GUI
'''
l = Label(root,text="DinoPass Client v0.1", font=("Impact",24), bg="gray")
l.pack(padx=80,pady=15)
t = Label(root,textvariable=ptype,font=("Helvetica",12), bg="gray")
t.pack()

'''
Creates a textbox and populates it with the password variable
'''
e = Entry(root,textvariable=password, font=("Helvetica",16))
e.pack(pady=10)

'''
Used to track last ptype retrieved.
'''
simple = True;


def addToClipBoard(text):
    command = '@echo off | echo ' + text.strip() + '| clip'
    os.system(command)

'''
Sets ptype depending on whether simple is True or False
'''
def update_ptype():
    global simple, ptype
    if simple:
        ptype.set("Simple Password")
    else:
        ptype.set("Complex Password")

'''
Gets a simple password using the dinopass API, and appends an exclamation mark to the end.
The password is then automatically copied to the users clipboard.
'''
def get_password():
    global password, simple
    r = requests.get("http://www.dinopass.com/password/simple")
    p = r.text.capitalize() + '!'
    password.set(p)
    root.clipboard_clear()
    root.clipboard_append(password.get())
    simple = True
    update_ptype()

'''
Gets a strong password using the dinopass API, the password is then automatically copied to the users clipboard.
'''
def get_password2():
    global password, simple
    r = requests.get("http://www.dinopass.com/password/strong")
    p = r.text
    password.set(p)
    root.clipboard_clear()
    root.clipboard_append(password.get())
    simple = False
    update_ptype()

'''
Retrieves a simple or strong password from Dinopass depending on the value of simple.
'''
def get_p(event):
    global simple
    if simple:
        get_password()
    else:
        get_password2()

'''
Changes simple to !simple
'''
def switch_type(event):
    global simple
    if simple:
        simple = False
    else:
        simple = True
    update_ptype()

'''
Sets the colour of the frame the buttons will be placed in.
'''
f = Frame(root,bg="gray")

'''
Creates a button to retrieve a simple password and adds it to frame f.
'''
b = Button(f,text="Simple Password",command=get_password, font=("Helvetica",16))
b.pack(pady=15, side=LEFT)


'''
Creates a button to retrieve a strong password, and adds it to frame f.
'''
b2 = Button(f,text="Strong Password",command=get_password2, font=("Helvetica",16))
b2.pack(pady=15, side=RIGHT)

'''
Adds the frame to the root frame.
'''
f.pack()

'''
Gets a password using the dinopass API if the return key is pressed.
'''
root.bind('<Return>',get_p)

'''
Changes the password type retrieved if any arrow key is pressed.
'''
root.bind('<Left>',switch_type)
root.bind('<Right>',switch_type)
root.bind('<Up>',switch_type)
root.bind('<Down>',switch_type)

#init
get_password() #Sets a default password

root.mainloop() #Keeps the program running until the GUI is closed.
