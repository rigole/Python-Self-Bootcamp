#from cProfile import label
from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)


my_label = Label(text="Here is a label", font=("Arial",24, "bold"))
my_label.pack()

def button_clicked():
    print("I got cliked")

button = Button(text="Click here", command=button_clicked)
button.pack()


window.mainloop()