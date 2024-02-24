import customtkinter as ctk

def button_event():
    print("button pressed")



window = ctk.CTk()

window.title("Password Generator V2")
window.geometry('800x600')
ctk.set_appearance_mode("dark")


frame = ctk.CTkFrame(master=window)
frame.pack(pady=20, padx=60, fill="both", expand=True)


button = ctk.CTkButton(frame, text="Button", command=button_event)
button.pack()


window.mainloop()