from tkinter import *
window = Tk()
window.title("Event Handler")
window.geometry("100x100")
def HandleKeyPress(event):
    print(event.char)

window.bind("<Key>", HandleKeyPress)

def HandleClick(event):
    print("\nButton was clicked")

button = Button(window, text="Click Me")
button.pack()

button.bind("<Button-1>", HandleClick)
window.mainloop()
