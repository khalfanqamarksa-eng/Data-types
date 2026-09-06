from tkinter import *
window = Tk()
window.title("Login App")
window.geometry("400x400")

frame = Frame(master=window, height=200, width=360, bg = "#d0efff")
lbl1 = Label(frame, text="Full name", bg = "#3895D3", fg ='white', width = 12)
lbl2 = Label(frame, text="Email", bg = "#3895D3", fg ='white', width = 12)
lbl3 = Label(frame, text="Password", bg = "#3895D3", fg ='white', width = 12)

name_entry = Entry(frame)
email_entry = Entry(frame)
password_entry = Entry(frame, show="*")

def display():
    name = name_entry.get()
    greet = "Hello " + name
    message = "Congratulations! You have successfully logged in."
    textbox.insert(END, greet)
    textbox.insert(END, message)
textbox = Text(bg="#BEBEBE", fg="black")
btn = Button(text = 'Create Account', command = display, bg="red")

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
lbl2.place(x=20, y=60)
lbl3.place(x=20, y=100)
name_entry.place(x=150, y=20)
email_entry.place(x=150, y=60)
password_entry.place(x=150, y=100)
btn.place(x=150, y=140)
textbox.place(x=20, y=180)
window.mainloop()