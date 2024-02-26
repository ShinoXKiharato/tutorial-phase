import random
from string import *
import string
import tkinter as tk
from tkinter import *
from PIL import Image
import time

string.ascii_letters   

import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

window = ctk.CTk()
window.title("Password Generator V2")
window.geometry('800x600')

#--------------
file = "password_gen\\skeleton-meme.gif"
info = Image.open(file)

img1 = PhotoImage(file="password_gen\\skeleton-memetbh.png")

frames = info.n_frames  # number of frames

photoimage_objects = []
for i in range(frames):
    obj = tk.PhotoImage(file=file, format=f"gif -index {i}")
    photoimage_objects.append(obj)

loop = None
def animation(current_frame=0, loop=None):
    imglabel.configure(width=220,height=220)
    image1 = photoimage_objects[current_frame]
    
    imglabel.configure(image=image1)
    current_frame = current_frame + 1

    if current_frame == frames:
        current_frame = 0

    loop = frame2.after(50, lambda: animation(current_frame, loop))

def stop_animation():
    if loop is not None:
        time.sleep(3)
        frame2.after_cancel(loop)

#------------

def submit():

    endbox.configure(state="normal")
    p = True
    while p == True:
        generated_password = ""
        password_lenght = 0
        if optional.get():  # Check if optional entry is not empty
            try:
                password_lenght = int(optional.get())
            except ValueError:
                password_lenght = len(entrybox.get())
        else:
            password_lenght = len(entrybox.get())

        user_input = entrybox.get()
        len_u_input = len(user_input) 
        char_counts = {}

        while len(generated_password) <= (password_lenght -1):    

            if (pnc.get() == 1) and (nmb.get() == 1):
                choices = [random.choice(string.ascii_letters) if random.choice(string.ascii_letters) != generated_password[-1:] else random.choice(string.ascii_letters)
                    , user_input[::random.randint(1, (6 or 8)) if len_u_input >= 5 else random.randint(1, (2 or 3))]
                    , random.choice(string.punctuation)
                    , random.choice(string.digits)]
                
                weights = [0.4 if password_lenght >= 12 else 0.5, 0.5 if password_lenght >= 12 else 0.4, 0.25 if password_lenght >= 12 else 0.55, 0.25 if password_lenght >= 12 else 0.55]
                next_char = random.choices(choices, weights=weights)[0]

            elif (pnc.get() == 1):
                choices = [random.choice(string.ascii_letters) if random.choice(string.ascii_letters) != generated_password[-1:] else random.choice(string.ascii_letters)
                    , user_input[::random.randint(1, (6 or 8)) if len_u_input >= 5 else random.randint(1, (2 or 3))]
                    , random.choice(string.punctuation)]
                
                weights = [0.45 if password_lenght >= 12 else 0.5, 0.5 if password_lenght >= 12 else 0.435, 0.3 if password_lenght >= 12 else 0.55]
                next_char = random.choices(choices, weights=weights)[0]
            elif (nmb.get() == 1):
                choices = [random.choice(string.ascii_letters) if random.choice(string.ascii_letters) != generated_password[-1:] else random.choice(string.ascii_letters)
                    , user_input[::random.randint(1, (6 or 8)) if len_u_input >= 5 else random.randint(1, (2 or 3))]
                    , random.choice(string.digits)]
                
                weights = [0.45 if password_lenght >= 12 else 0.58, 0.5 if password_lenght >= 12 else 0.45, 0.3 if password_lenght >= 12 else 0.525]
                next_char = random.choices(choices, weights=weights)[0]
            else:
                choices = [random.choice(string.ascii_letters) if random.choice(string.ascii_letters) != generated_password[-1:] else random.choice(string.ascii_letters)
                    , user_input[::random.randint(1, (6 or 8)) if len_u_input >= 5 else random.randint(1, (2 or 3))]]
                
                weights = [0.65 if password_lenght >= 8 else 0.55, 0.5 if password_lenght >= 8 else 0.6]
                next_char = random.choices(choices, weights=weights)[0]

            if (
                (user_input in generated_password + next_char and len(user_input) > 2)
                or (next_char.upper() in char_counts and char_counts[next_char.upper()] >= 5)
            ):
                continue

            char_counts[next_char.upper()] = char_counts.get(next_char.upper(), 0) + 1

            generated_password += next_char

        endbox.insert('1.0', generated_password + "   <- is " + str(len(generated_password)) +" Characters long \n")
        p = False
        endbox.configure(state=DISABLED)
    stop_animation()
#----------------

titlelable = ctk.CTkLabel(window, text="Password Generator V2", font=("Arial", 18))
titlelable.pack(pady=10)
#------------
frame = ctk.CTkFrame(window)
frame.pack(fill="both", expand=True)

frame1 = ctk.CTkFrame(frame)
frame1.pack(fill="both", pady=15, padx=30) 
#------------

entrybox = ctk.CTkEntry(frame1, width=200, height=30, placeholder_text="Enter a Prompt",)
entrybox.pack(padx=12,pady=12, side=LEFT)

submit_button = ctk.CTkButton(frame1, text="Submit", command=lambda: [(submit(), animation(current_frame=0, loop=loop))], width=60, font=("Arial", 14))
submit_button.pack(side=LEFT)

optional = IntVar()
optional = ctk.CTkEntry(frame1, placeholder_text="Lenght (5)", width=75, height=30)
optional.pack(pady=12, padx=12, side=LEFT)

pnc = IntVar()
checkboxPun = ctk.CTkCheckBox(master=frame1, 
                           text="Punctuation", 
                           #command=punctuation, 
                           variable=pnc,
                           onvalue=1,
                           offvalue=0,
                           font=("Arial", 14))

checkboxPun.pack(pady=12, padx=20, side="right")

nmb = IntVar()
checkboxNum = ctk.CTkCheckBox(master=frame1, 
                           text="Numbers", 
                           #command=number, 
                           variable=nmb,
                           onvalue=1,
                           offvalue=0,
                           font=("Arial", 14))

checkboxNum.pack(pady=12, padx=15, side="right")

asklabel = ctk.CTkLabel(frame1, text="Add:", font=("Arial", 16))
asklabel.pack(pady=12, padx=15, side="right")

#----------------

frame2 = ctk.CTkFrame(frame, width=600, height=400)
frame2.pack(fill="both",pady=15, padx=30)

endbox = ctk.CTkTextbox(frame2,
                        state="disabled",
                        font=("Arial", 16),
                        width=500)
endbox.pack(side=LEFT,pady=10, padx=12)

imglabel = Label(frame2,
                image=img1,
                width=220, height=220,
                background="#292929"
                )
imglabel.pack(side=RIGHT, pady=5, padx=30)




width = frame2.winfo_width()
height = frame2.winfo_height()

print(f"Frame size: {width} x {height}")

window.mainloop()