from  tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
               'i', 'j', 'k', 'l', 'm,',
         'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)
    password_letters= [random.choice(letters) for _ in range (nr_letters)]
    password_numbers= [random.choice(numbers) for _ in range (nr_numbers)]
    password_symbols= [random.choice(symbols) for _ in range (nr_symbols)]
    password_list=password_letters+password_numbers+password_symbols
    random.shuffle(password_list)
    password= "".join(password_list)
    password_entry.delete(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    done_password=f"{website}|{email}|{password}\n"

    if len(website)==0 or len(email)==0:
        messagebox.showerror("Error","Please make sure you haven't left any fields empty")
    else:
        is_ok=messagebox.askokcancel(website,f"These are the detailed entered:"
                                       f"\n Email:{email} \nPassword:{password}\n is it ok to save?")
        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(done_password)
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas =Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

website_label = Label( text="Website:",font=("Arial", 20))
website_label.grid(row=1, column=0)

email_label = Label( text="Email/Username:",font=("Arial", 20))
email_label.grid(row=2, column=0)

password_label = Label( text="Password:",font=("Arial", 20))
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1,columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1,columnspan=2)
email_entry.insert(0,"adejaredavid302@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

password_button=Button(text="Generate password",command=password_generator)
password_button.grid(row=3, column=2)

password_saver=Button(text="Add",width=36)
password_saver.grid(row=4, column=1,columnspan=2,command=save_password)


window.mainloop()