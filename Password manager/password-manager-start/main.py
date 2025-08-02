from tkinter import *
from tkinter import messagebox
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save(): 

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="Please don't leave any fields empty!")

    else:
        with open("data.json", "w") as data_file:
            # json.dump(new_data, data_file, indent=4)        
            data = json.load(data_file)
            print
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            

       
    

    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
photo = PhotoImage(file="D:\Python\day29\password-manager-start\logo.png")
canvas.create_image(100, 100, image= photo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=("Arial", 10))
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", font=("Arial", 10))
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=("Arial", 10))
password_label.grid(column=0, row=3)


# Entries
website_entry = Entry(width=35)
website_entry .grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "unnati@gmail.com")
password_entry = Entry(width=21)
password_entry .grid(column=1, row=3, columnspan=2)
generate_button = Button(text="Generate Password", width=15)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()