import customtkinter as ctk

def button_event():
    print("button pressed")



window = ctk.CTk()

window.title("Password Generator V2")
window.geometry('800x600')
ctk.set_appearance_mode("dark")


frame = ctk.CTkFrame(master=window)
frame.pack(pady=20, padx=60, fill="both", expand=True)

frame1 = ctk.CTkFrame(master=frame, width=600, height=400)
frame1.pack(side="left",padx=20)

button = ctk.CTkButton(frame, text="Button", command=button_event)
button.pack(pady=70)


window.mainloop()