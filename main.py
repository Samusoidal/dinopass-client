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
password = StringVar() 
password_type = StringVar()

'''
Adds a label and packs it into the GUI
'''
root_label = Label(root,text="DinoPass Client v0.1", font=("Impact",24), bg="gray")
root_label.pack(padx=80,pady=15)
type_label = Label(root,textvariable=password_type,font=("Helvetica",12), bg="gray")
type_label.pack()

'''
Creates a textbox and populates it with the password variable
'''
password_entry = Entry(root,textvariable=password, font=("Helvetica",16))
password_entry.pack(pady=10)


def addToClipBoard(text):
    command = '@echo off | echo ' + text.strip() + '| clip'
    os.system(command)


'''
Gets a simple password using the dinopass API, and appends an exclamation mark to the end.
The password is then automatically copied to the users clipboard.
'''
def get_simple_password():
    global password
    request= requests.get("http://www.dinopass.com/password/simple")
    retrieved_password = request.text.capitalize() + '!'
    password.set(retrieved_password)
    root.clipboard_clear()
    root.clipboard_append(password.get())
    password_type.set("Simple Password")

'''
Gets a strong password using the dinopass API, the password is then automatically copied to the users clipboard.
'''
def get_strong_password():
    global password
    request = requests.get("http://www.dinopass.com/password/strong")
    retrieved_password = request.text
    password.set(retrieved_password)
    root.clipboard_clear()
    root.clipboard_append(password.get())
    password_type.set("Complex Password")

'''
Retrieves a simple or strong password from Dinopass depending on the value of simple.
'''
def get_password(event):
    if password_type("Simple Password"):
        get_simple_password()
    else:
        get_strong_password()

'''
If the password type is currently complex password it is converted to simple password and vice-versa.
'''
def switch_type(event):
    if password_type.get() == "Simple Password":
        password_type.set("Complex Password")
    else:
        password_type.set("Simple Password")

'''
Creates a frame and sets the colour of the frame the buttons will be placed in.
'''
button_frame = Frame(root,bg="gray")

'''
Creates a button to retrieve a simple password and adds it to frame f.
'''
simple_button = Button(button_frame,text="Simple Password",command=get_simple_password, font=("Helvetica",16))
simple_button.pack(pady=15, side=LEFT)


'''
Creates a button to retrieve a strong password, and adds it to frame f.
'''
strong_button = Button(button_frame,text="Strong Password",command=get_strong_password, font=("Helvetica",16))
strong_button.pack(pady=15, side=RIGHT)

'''
Adds the frame to the root frame.
'''
button_frame.pack()

'''
Gets a password using the dinopass API if the return key is pressed.
'''
root.bind('<Return>',get_password)

'''
Changes the password type retrieved if any arrow key is pressed.
'''
root.bind('<Left>',switch_type)
root.bind('<Right>',switch_type)
root.bind('<Up>',switch_type)
root.bind('<Down>',switch_type)

#init
get_simple_password() #Sets a default password

root.mainloop() #Keeps the program running until the GUI is closed.
