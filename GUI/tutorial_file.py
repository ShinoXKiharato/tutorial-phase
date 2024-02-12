from msilib.schema import Icon
from tkinter import *
from turtle import back, right

# Widgets = GUI Elements: buttons, textboxes, labels, images etc.
# Windows = serves as a container to hold or contain those widgets

window = Tk() # instantiate an instance of a window
window.geometry("640x640") # size of window
window.title("Yua's first GUI") #window title
window.config(background="dark blue") #change backgroudn color



photo = PhotoImage(file="GUI\\anime01.png")
resized_photo = photo.subsample(6,6)
#------------------------------------- Icon
'''
icon = PhotoImage(file="icon.png")
window.iconphoto(True, icon)
icon_ref = icon''' #doesn't work, file not found 

#----------------------------------------------------

#label = an area widget that holds text and/or an image within a window
'''
label = Label(window, text="Hello World",
              font=('Arial',40,'bold'),
                fg='red', bg="black",#foreground and background
                relief=RAISED, bd=10, #border width 10 and relief changes style
                padx=20, pady=20,
                image=resized_photo,
                compound="bottom") 
label.pack()'''
#label.place(x=100,y=100)

#----------------------------------------------------

#Buttons = you click it, then it does stuff
'''
count = 0

def click():
    global count
    count += 1
    print(count)
    print("You clicked the button!")
button = Button(window,
                text="Click me",
                command=click,
                font=("Comic-Sans", 30),
                fg="green",
                bg="black",
                activeforeground="green",
                activebackground="black",
                #state=DISABLED disables button
                image=resized_photo,
                compound="bottom")
button.pack()
'''

#-----------------------------------------------

# entry widget = textbox that accepts a single line of user input
'''
def submit():
    username = entry.get()
    print("Hello "+username)
    entry.config(state=DISABLED) #to disable box after entry

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1, END) # second to last, last character I only removes last char


entry = Entry(window,
              font=("Ariel",35),
              fg="red",
              bg="black",
              #show="*" only displays * basically hides the text
              )
entry.insert(0, 'Enter Username: ')
entry.pack(side=LEFT)


submit_button = Button(window, text="Submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="Delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="Backspace", command=backspace)
backspace_button.pack(side=RIGHT)
'''
# -----------------------------------------------------------

# Checkbox
'''
def display():
    if (x.get()==1):
        print("You agreed")
    else:
        print("You don't agree")
x = IntVar()
check_button = Checkbutton(window,
                           text="Yes",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial',20),
                           fg='red', bg="black",
                           activeforeground='red', activebackground='black',
                           padx=25, pady=10,
                           image=resized_photo, compound="left")
check_button.pack()'''
#----------------------------------------------------------


window.mainloop() #place window on computer screen, listen for events

