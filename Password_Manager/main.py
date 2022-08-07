import email
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
#Password generator
# u(#d86mo3le1sjx
def password_generator():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','#','$','&','%','(',')', '*','+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    #for char in range(nr_letters):
    #
    # password_list.append(random.choice(letters))
    
    #for char in range(nr_symbols):
    #    password_list += random.choice(symbols)
    
    #for char in range(nr_numbers):
    #    password_list += random.choice(numbers)
    
    
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    #print(f"Your password is: {password}")
    password_entry.insert(0, password)

    #for char in password_list:
        #password += char
    

    #Saving Password
    pyperclip.copy(password)

def save():
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_password = {
        website:{
            "email":email,
            "password": password,
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please make sure all fields are not empty")
    else:
        #is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \n Is it okay to save")
        #if is_ok:
        try:
            with open("data.json", "r") as data_file:
            #json.dump(new_p assword, data_file, indent=4)
            #data_file.write(f"| {website} | {email} | {password}\n")
            
            #reading old data
                data = json.load(data_file)
            
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_password, data_file, indent=4)
            
            
        else:
            
            #Update old data with new data
            data.update(new_password)
             
            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
                #print(data)
                
        finally:
            
                website_entry.delete(0, END)
                password_entry.delete(0, END)



def find_password():
    pass
    website = website_entry.get()
    with open("data.json") as data_file:
        data = json.load(data_file)
        if website in data:
             email = data[website]["email"]
             password = data[website]["password"]
             messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")




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
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "foplacide@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, columnspan=1)

# Buttons
search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(row=3, column=2, columnspan=2)
add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)













window.mainloop()