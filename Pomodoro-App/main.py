
from email.mime import image
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

window = Tk()
window.title("Pomorodo")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=400, height=424, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(200, 202, image=tomato_img)
canvas.create_text(203, 230, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()













window.mainloop()