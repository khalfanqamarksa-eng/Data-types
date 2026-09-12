from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Virus Detector")
window.geometry("200x200")
def msg():
    messagebox.showwarning("STOP!", "Virus Detected")
btn = Button(window, text="Scan for Viruses", command=msg)
btn.place(x=40, y=80)
window.mainloop()