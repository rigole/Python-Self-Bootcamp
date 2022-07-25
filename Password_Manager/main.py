from tkinter import *
from tkinter import messagebox
import random

#Password generator
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','&','%','(',')', '*','+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)


#Saving Password

def save():
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please make sure all fields are not empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \n Is it okay to save")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"| {website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


        
    



























#Tkinter interface

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#canvas
canvas = Canvas(height=200, width=200)
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
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "foplacide@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, columnspan=1)

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)













window.mainloop()