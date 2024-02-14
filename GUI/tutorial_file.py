from email.mime import image
from msilib.schema import Icon
from tabnanny import verbose
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

giftimg = PhotoImage(file="GUI\\1301.png")
coupimg = PhotoImage(file="GUI\\1302.png")
snowimg = PhotoImage(file="GUI\\1303.png")
listImages = [giftimg, coupimg, snowimg]

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

# radio buttons =  similar to checkbox, but you can only select one from a group.
'''
x = IntVar()
food = ["pizza","hamburger","hotdog"]

def order():
    if(x.get() == 0):
        print("You ordered pizza.")
    elif(x.get() == 1):
        print("You ordererd a Hamburger")
    elif(x.get() == 2):
        print("You ordered a Hotdog")
    else:
        print("Huh?")

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                            text=food[index], # adds text to radio buttons
                            variable=x, # groups radibuttons together if they share the same variable
                            value=index, #this assigns each radiobutton a different value
                            padx=25, pady=10,
                            font=("Impact", 35),
                            image=listImages[index], compound="right", #Adds image to the radiobutton
                            indicatoron=0, #eliminate circle indicators
                            width = 375,
                            command=order #this sets the command for the radio buttons
                            )
    radiobutton.pack(anchor=W)'''
#-------------------------------------------------------------------
#sliding scale
'''
coldlabel = Label(image=snowimg)
coldlabel.pack()
def submit():
    print("The temp is "+ str(scale.get())+ "degrees C")
scale = Scale(window, 
              from_=100,
              to=0,
              length=500, # increases the scales lenght
              orient=VERTICAL, #sets the scale vertically up
              font=("Consolas",20),
              tickinterval=10, #adds numeric indicators for value
              showvalue=0, #hides current value on the slider itself
              resolution=5, #incremend of slider
              troughcolor='blue', #color of inner 
              fg='#FF1C00',
              bg='#111111'

              )
scale.set(((scale['from']-scale['to'])/2)+scale['to']) #makes it so the scale always starts in the middle
scale.pack()

giftlabel = Label(image=giftimg)
giftlabel.pack()


button = Button(window, text="submit",command=submit)
button.pack()'''

#---------------------------------------------------------------

# listbox = A listing of selectable text items within it's own container
'''
def submit():
    food = []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print("You have ordered: ")

    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(), entrybox.get())
    listbox.config(height=listbox.size())

def delete():
    #listbox.delete(listbox.curselection())
    for index in reversed(listbox.curselection()): #deletes from a reversed order to delete all selected indexes, because index change when one is deleted.
        listbox.delete(index)
    listbox.config(height=listbox.size())

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=('Constantia', 35),
                  width=12,
                  selectmode=MULTIPLE,)
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

listbox.config(height=listbox.size()) # dinamically changes size of list box

entrybox = Entry(window, 
                 )
entrybox.pack()

submitButton = Button(window, text="Submit", command=submit)
submitButton.pack()

addButton = Button(window, text="Add", command=add)
addButton.pack()
deleteButton = Button(window, text="delete", command=delete)
deleteButton.pack()'''

#--------------------------------------------------

# messagebox 

#from tkinter import messagebox #import messagebox libary

#def click():
    #messagebox.showinfo(title="This is an info message box", message="You got a virus lol")
    #messagebox.showwarning(title="WARNING", message="You got a virus lol")
    #messagebox.showerror(title="ERROR", message="Something went wrong")

    #if messagebox.askokcancel(title="ask ok cancel", message="Do you want to slice tha kid?"):
        #print("You killed tha kidd")
    #else:
        #print("You canceld a thing")
'''
    if messagebox.askretrycancel(title="ask ok retry cancel", message="Do you want to retry?"):
        print("You retried a thing")
    else:
        print("You canceled a thing")'''
    
    #if messagebox.askyesno(title="Ask yes or no", message="Do you want to eat tha cake?"): #returns a bool value
        #print("YOu ate tha cake")
    #else:
        #print("I guess no cake today")
'''
    answer = messagebox.askquestion(title="Ask question", message="Do you like pie?") #returns a string with yes / no
    if(answer == 'yes'):
        print('Pie pie pie pie')
    else:
        print("no pie ):")'''
    
    #answer = messagebox.askyesnocancel(title="Ask yes no cancel", message="Do you like to code?",icon='warning') #returns True, False or None

    #if(answer==True):
        #print("I like to code too")
    #elif(answer==False):
        #print("Burn tha witch")
    #else:
        #print("You dodged me ):")
'''
button = Button(window, command=click, text="Click me")
button.pack()
'''

#------------------------------------------------------

# Colorchooser
'''
from tkinter import colorchooser #submodule

def click():
    window.config(colorchooser.askcolor()[1]) #changes background color

button = Button(window,
                text="click me",
                command=click,
                )
button.pack()
'''
#----------------------------------------------------

# Text Area

# text widget = functions like a text area, you can enter multiple linse of text
'''
def submit():
    input = text.get("1.0", END)
    print(input)

text = Text(window,
            bg="light yellow",
            font=("Ink Free", 20),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="purple"
            )
text.pack()

button = Button(window, command=submit, text="submit")
button.pack()'''

#-----------------------------------------------

# File dialouge, open and read files
'''
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\tobia\\OneDrive\\Dokumente\\GitHub\\tutorial-phase\\GUI",
                                          title="Open file",
                                          filetypes= (("text files", "*.txt"),
                                          ("all files", "*.*")))
    file = open(filepath, 'r')
    print(file.read())
    file.close()
window = Tk()


button = Button(text="Open", command=openFile)
button.pack()
window.mainloop()'''
# -------------------------------------- 1H 50M


window.mainloop() #place window on computer screen, listen for events

