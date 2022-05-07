from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo


def user_message():

    if len(u_var.get()) != 0 and len(p_var.get()) != 0:
        showinfo("Hello", f"Login successful")
    else:
        showinfo("Uh, oh!", f"Who are you?")


# call tkinter class
window = Tk()
window.geometry("300x225")
window.title("Password Manager")


u_lbl = Label(window, text="Username:", font=("monospace bold", 10))
u_lbl.place(x=50, y=40)

# creates text box for user input
u_var = StringVar()
u_txt = Entry(window, width=20, textvariable=u_var)
u_txt.place(x=125, y=42)


p_lbl = Label(window, text="Password:", font=("monospace", 10))
p_lbl.place(x=50, y=75)

# creates text box for user input
p_var = StringVar()
p_txt = Entry(window, width=20, textvariable=p_var)
p_txt.place(x=125,y=77)

# our button
btn = Button(window, text="Login", width="15", bg="gray", command=user_message)
btn.place(x=100,y=150)

window.mainloop()

