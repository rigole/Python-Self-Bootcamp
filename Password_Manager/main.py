from tkinter import *

#Tkinter interface

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#canvas
canvas = Canvas(height=200, width=200, highlightthickness=0)
project_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=project_image)
canvas.grid(row=0, column=1)


#Labels
website_label = Label(text="Website Url")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="password")
password_label.grid(row=3, column=0)

# Input
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)















window.mainloop()