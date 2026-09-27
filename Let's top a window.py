from tkinter import *
root = Tk()
root.title("Top Window")
root.geometry("400x300")

def topwin():
    top = Toplevel(root)
    top.title("New Window")
    top.geometry("200x150")

    l2= Label(top, text="This is a new window")
    l2.pack()
    top.mainloop()
l = Label(root, text="This is the main window")
l.pack()
btn = Button(root, text= "Open New Window", command=topwin)
btn.pack()
root.mainloop()