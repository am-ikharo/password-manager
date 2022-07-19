import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char_ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char__ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    password_area.insert(0, f"{password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_name = website_text_box.get()
    username = username_text_box.get()
    password = password_area.get()
    new_data = {
        web_name: {
            "email": username,
            "password": password
        }
    }

    if web_name == "" or username == "" or password == "":
        messagebox.showerror(title="Oop", message="Please don't leave any field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:

            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_text_box.delete(0, END)
            password_area.delete(0, END)
            website_text_box.focus()

def find_password():
    web_name = website_text_box.get()
    try:
        with open("data.json", "r") as data_file:
            read_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="Data File does not exist")
    else:
        try:
            search_website = read_data[web_name]
        except KeyError:
            messagebox.showerror(title="Oop", message="No details for the website exist")
        else:
            search_email = search_website["email"]
            search_password = search_website["password"]
            messagebox.askokcancel(title=f"{web_name}", message=f"email: {search_email}\n password: {search_password}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")

window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=220, height=220, bg="white", highlightthickness=0)
key_image = PhotoImage(file="logo.png")
canvas.create_image(110, 110, image=key_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ", bg="white")
website_label.grid(column=0, row=1)

website_text_box = Entry(width=35)
website_text_box.grid(column=1, row=1, columnspan=2)
website_text_box.focus()

username_label = Label(text="Email/username: ", bg="white")
username_label.grid(column=0, row=2)

username_text_box = Entry(width=35)
username_text_box.grid(column=1, row=2, columnspan=2)
username_text_box.insert(0, "m2ikharo1994@gmail.com")

password_label = Label(text="Password: ", bg="white")
password_label.grid(column=0, row=3)

password_area = Entry(width=23)
password_area.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", bg="white", command=generate_password)
generate_password_button.grid(column=2, row=3)

search_button = Button(text="Search", bg="white", width=10, command=find_password)
search_button.grid(column=2, row=1, sticky=E)

add_button = Button(text="Add", bg="white", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)





window.mainloop()