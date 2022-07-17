from tkinter import *


def feet_to_cm():
    feet = float(feet_input.get())
    cm = feet * 30.48
    cm_result_label.config(text=f"{cm}")

window = Tk()
window.title("Converter to kilometer")
window.config(padx=20, pady=20)

feet_input = Entry()
feet_input.grid(column=1, row=0)

feet_label = Label(text="Feet")
feet_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

cm_result_label = Label(text="0")
cm_result_label.grid(column=1, row=1)


cm_label = Label(text="Cm")
cm_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=feet_to_cm)
calculate_button.grid(column=1, row=2)


window.mainloop()