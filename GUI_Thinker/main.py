""" 
import tkinter

window = tkinter.Tk()
window.title("My first UI program")
window.minsize(width=500, height=300)
#

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))

my_label.pack(side="right")

window.mainloop()



def add(*args):
    total = 0
    for i in args:
        
        total += i
        
    return total

print(add(12, 15, 25))
"""




from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)


my_label = Label(text="Here is a label", font=("Arial",24, "bold"))
#my_label.pack(side="left")


button = Button(text="Click here")
button.pack()
