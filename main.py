import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    password_entry.delete(0, tkinter.END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #   password += char

    password_entry.insert(tkinter.END, password)
    pyperclip.copy(password)

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def handleSearch():
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
            messagebox.showinfo(title=f"{website.get()}", message=f"Email: {data[website.get()]['email']}\n"
                                                                  f"Password: {data[website.get()]['password']}")
    except FileNotFoundError:
        messagebox.showinfo(title="Not Found", message="Data is currently empty.")
    except KeyError as error_message:
        messagebox.showinfo(title="Not Found", message=f"Data for {error_message} not found.")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    new_data = {
        website.get(): {
            "email": email.get(),
            "password": password_entry.get()
        }
    }
    if len(website.get()) == 0 or len(password_entry.get()) == 0 or len(email.get()) == 0:
        messagebox.showinfo(title="Error", message="Cannot leave the blank empty")
    else:
        if messagebox.askokcancel(title="Want to save?",
                                  message=f"Email: {email.get()}\nPassword:{password_entry.get()}"):
            try:
                with open("data.json", mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
            messagebox.showinfo(title="Message", message="Your password is saved!")
        website.delete(0, tkinter.END)
        password_entry.delete(0, tkinter.END)

# Note


'''
    json.dump() to save data in JSON form
    json.load() will convert json to dict, don't forget to change the mode 
    json.update()
'''
# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.config(padx=50, pady=50, bg="white")
window.title("Password Generator")

canvas = tkinter.Canvas(width=200, height=200, bg="white", highlightthickness=0)
img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

#
label_1 = tkinter.Label()
label_1.config(text="Website:", bg="white")
label_1.grid(row=1, column=0)
label_2 = tkinter.Label()
label_2.config(text="Email/Username:", bg="white")
label_2.grid(row=2, column=0)
label_3 = tkinter.Label()
label_3.config(text="Password", bg="white")
label_3.grid(row=3, column=0)
#
website = tkinter.Entry()
website.config(width=21)
website.focus()
website.grid(column=1, row=1)
email = tkinter.Entry()
email.config(width=35)
email.insert(tkinter.END, "your_email@gmail.com")
email.grid(row=2, column=1, columnspan=2)
password_entry = tkinter.Entry(width=21)
password_entry.grid(column=1, row=3)


search_btn = tkinter.Button()
search_btn.config(command=handleSearch, text="Search")
search_btn.grid(column=2, row=1)
pass_btn = tkinter.Button()
pass_btn.config(command=generate_password, text="Generate Password")
pass_btn.grid(column=2, row=3)
add_btn = tkinter.Button()
add_btn.config(command=add_password, text="Add", width=36)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
