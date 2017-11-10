import requests, os
from tkinter import *

root = Tk()
root.configure(background="gray")
root.title("DinoPass Client")

pwd = StringVar()
ptype = StringVar()

l = Label(root,text="DinoPass Client v0.1", font=("Impact",24), bg="gray")
l.pack(padx=80,pady=15)
t = Label(root,textvariable=ptype,font=("Helvetica",12), bg="gray")
t.pack()

e = Entry(root,textvariable=pwd, font=("Helvetica",16))
e.pack(pady=10)

simple = True;

def addToClipBoard(text):
    command = '@echo off | echo ' + text.strip() + '| clip'
    os.system(command)

def update_ptype():
    global simple, ptype
    if simple:
        ptype.set("Simple Password")
    else:
        ptype.set("Complex Password")
    
def get_password():
    global pwd, simple
    r = requests.get("http://www.dinopass.com/password/simple")
    p = r.text.capitalize() + '!'
    pwd.set(p)
    root.clipboard_clear()
    root.clipboard_append(pwd.get())
    simple = True
    update_ptype()

def get_password2():
    global pwd, simple
    r = requests.get("http://www.dinopass.com/password/strong")
    p = r.text
    pwd.set(p)
    root.clipboard_clear()
    root.clipboard_append(pwd.get())
    simple = False
    update_ptype()

def get_p(event):
    global simple
    if simple:
        get_password()
    else:
        get_password2()

def switch_type(event):
    global simple
    if simple:
        simple = False
    else:
        simple = True
    update_ptype()
        
f = Frame(root,bg="gray")

b = Button(f,text="Simple Password",command=get_password, font=("Helvetica",16))
b.pack(pady=15, side=LEFT)

b2 = Button(f,text="Strong Password",command=get_password2, font=("Helvetica",16))
b2.pack(pady=15, side=RIGHT)

f.pack()

root.bind('<Return>',get_p)

root.bind('<Left>',switch_type)
root.bind('<Right>',switch_type)
root.bind('<Up>',switch_type)
root.bind('<Down>',switch_type)

#init
get_password()

root.mainloop()
