from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import json
import random

# --------------------------------------------- PASSWORD GENERATOR -------------------------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_symbol + password_number
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    return password


# -------------------------------------------------- SAVE PASSWORD -------------------------------------------------- #


def add_password():
    user = user_entry.get()
    user.lower()
    website = website_entry.get()
    website.lower()
    email = email_entry.get()
    password = password_entry.get()

    # Create the inner dictionary containing email and password
    inner_dict = {
        website.lower(): {
            "Email": email,
            "password": password,

        }
    }

    # Create the outer dictionary with user_lower as the key and the inner_dict as the value
    new_data = {
        user.lower(): {
            **inner_dict
        }
    }
    if len(user) == 0 or len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="ERROR", message="Please make sure you've filled all the entries.")

    else:
        is_ok = messagebox.askokcancel(title="CONFORMATION", message=f"Entered Details:\n\nName: {user}\n"
                                                                     f"Website: {website}\n"
                                                                     f"Email: {email}\n"
                                                                     f"Password: {password}\n\nAre you Sure?")
        if is_ok:
            try:
                with open("Data.json", "r") as data_file:
                    # reading from data
                    data = json.load(data_file)
            except FileNotFoundError:
                messagebox.showinfo(message="There Exits No Such User.\n\n "
                                            "Please Register before using the Application.")

            else:
                if user.lower() in data:
                    data[user.lower()].update(inner_dict)
                else:
                    messagebox.showinfo(message="There Exits No Such User.\n\n "
                                                "Please Register before using the Application.")

                # adding new new data
                with open("Data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                user_entry.delete(0, END)
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


# -------------------------------------------------- FIND PASSWORD -------------------------------------------------- #


def search_details():
    user = user_entry.get()
    users = user.lower()
    website = website_entry.get()
    check_website = website.lower()
    if len(users) == 0 or len(check_website) == 0:
        messagebox.showerror(message="Please Enter Details")
    else:
        try:
            with open("Data.json") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            messagebox.showinfo(title="ERROR", message="There Exists No Such Data File.")

        else:
            if users in data:
                if check_website in data[user]:
                    security_key = simpledialog.askinteger(title="Input", prompt="Enter the Security Key: ")
                    try:
                        with open("security_data.json") as load_security_key:
                            load_security_key = json.load(load_security_key)
                    except FileNotFoundError:
                        messagebox.showinfo(message="There Exist No Security File.")
                    else:
                        if security_key in load_security_key:
                            email = data[users][check_website]["email"]
                            password = data[users][check_website]["password"]
                            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
                        else:
                            messagebox.showinfo(message="You've Entered the wrong key.")
                else:
                    messagebox.showerror(message="There Exists No Such Directory in the Database.")
            else:
                messagebox.showinfo(title="FileNotFound", message="There Exists No Such User in the Database.")


# ------------------------------------------------ DELETE PASSWORD -------------------------------------------------- #


def delete_entry():
    user = user_entry.get()
    users_website = user.lower()
    website = website_entry.get()
    del_website = website.lower()
    if len(users_website) == 0 or len(del_website) == 0:
        messagebox.showerror(message="Please Enter Details")
    else:
        try:
            with open("Data.json") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            messagebox.showinfo(title="ERROR", message="There Exists No Such Data File.")

        else:
            if users_website in data:
                if del_website in data[users_website]:
                    is_yes = messagebox.askyesno(message=f"Are you sure you want to delete {del_website} Details?")
                    if is_yes:
                        security_key = simpledialog.askinteger(title="Input", prompt="Enter the Security Key: ")
                        try:
                            with open("security_data.json") as load_security_key:
                                load_security_key = json.load(load_security_key)
                        except FileNotFoundError:
                            messagebox.showinfo(message="There Exist No Security File.")
                        else:
                            if security_key in load_security_key:
                                del data[users_website][del_website]
                                messagebox.showinfo(title="DONE", message=f"Details for {del_website} are Deleted.")
                            else:
                                messagebox.showinfo(message="You've Entered the wrong key.")
                        with open('Data.json', 'w') as data_file:
                            json.dump(data, data_file, indent=2)
                else:
                    messagebox.showerror(message="There Exists No Such Directory in the Database.")
            else:
                messagebox.showinfo(title="FileNotFound", message="There Exists No Such User in the Database.")

# ------------------------------------------------ Security key ----------------------------------------------------- #


def security():
    key = simpledialog.askinteger(title="Input", prompt="Enter a Security Key:\n(Don't Forget the Security Key)")
    if key is not None:
        try:
            with open("security_data.json", "r") as security_data_file:
                security_data = json.load(security_data_file)
        except FileNotFoundError:
            security_data = [key]  # Initialize with the entered key
            with open("security_data.json", "w") as security_data_file:
                json.dump(security_data, security_data_file)
            return True
        else:
            if key not in security_data:
                security_data.append(key)
                with open("security_data.json", "w") as security_data_file:
                    json.dump(security_data, security_data_file)
                return True
            else:
                messagebox.showinfo(message="Key already exists.\nPlease choose a different key")


# --------------------------------------------------- New User ----------------------------------------------------- #
def new_user():
    def generate_new_user_password():
        new_password = generate_password()
        new_password_entry.insert(0, new_password)

    def add_new_user():
        user = new_user_entry.get()
        website = new_website_entry.get()
        email = new_email_entry.get()
        password = new_password_entry.get()

        inner_dict = {
            website.lower(): {
                "email": email,
                "password": password
            }
        }

        new_data = {
            user.lower(): {
                **inner_dict
            }
        }
        if len(user) == 0 or len(website) == 0 or len(email) == 0 or len(password) == 0:
            messagebox.showinfo(title="ERROR", message="Please make sure you've filled all the entries.")

        else:
            is_ok = messagebox.askokcancel(title="CONFORMATION", message=f"Entered Details:\n\nName: {user}\n"
                                                                         f"Website: {website}\n"
                                                                         f"Email: {email}\n"
                                                                         f"Password: {password}\n\nAre you Sure?")
            if is_ok:
                if security():
                    try:
                        with open("Data.json", "r") as data_file:
                            data = json.load(data_file)
                    except FileNotFoundError:
                        with open("Data.json", "w") as data_file:
                            json.dump(new_data, data_file, indent=4)
                            messagebox.showinfo(title="SUCCESS", message="New user added successfully.")
                            new_window.destroy()

                    else:
                        if user.lower() in data:
                            data[user.lower()].update(inner_dict)
                        else:
                            data[user.lower()] = inner_dict
                        with open("Data.json", "w") as data_file:
                            json.dump(data, data_file, indent=4)
                        messagebox.showinfo(title="SUCCESS", message="New user added successfully.")
                        new_window.destroy()

    new_window = Toplevel()
    new_window.title("New User Registration")
    new_window.config(padx=50, pady=50)

    new_canvas = Canvas(new_window, width=250, height=250)
    new_pass_img = PhotoImage(file="logo.png")
    new_canvas.create_image(125, 125, image=new_pass_img)
    new_canvas.grid(row=0, column=1)

    # Label
    heading = Label(new_window, text="New User Entry")
    heading.grid(row=1, column=1, sticky="EW")
    new_user_name = Label(new_window, text="User's Name:")
    new_user_name.grid(row=2, column=0, sticky="W")
    new_website_label = Label(new_window, text="Website:")
    new_website_label.grid(row=3, column=0, sticky="W")
    new_email_label = Label(new_window, text="Email/Username:")
    new_email_label.grid(row=4, column=0, sticky="W")
    new_password_label = Label(new_window, text="Password:")
    new_password_label.grid(row=5, column=0, sticky="W")

    # Entries
    new_user_entry = Entry(new_window)
    new_user_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
    new_user_entry.focus()
    new_website_entry = Entry(new_window)
    new_website_entry.grid(row=3, column=1, columnspan=2, sticky="EW")
    new_email_entry = Entry(new_window)
    new_email_entry.grid(row=4, column=1, columnspan=2, sticky="EW")
    new_password_entry = Entry(new_window)
    new_password_entry.grid(row=5, column=1, sticky="EW")

    # Buttons
    new_generate_button = Button(new_window, text="Generate Password", command=generate_new_user_password)
    new_generate_button.grid(row=5, column=2, sticky="EW")
    new_add_button = Button(new_window, text="Add", command=add_new_user)
    new_add_button.grid(row=6, column=1, columnspan=2, sticky="EW")

    new_window.mainloop()


# --------------------------------------------------- UI SETUP ------------------------------------------------------ #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(row=0, column=1)
# Label
user_name = Label(text="User's Name:")
user_name.grid(row=1, column=0, sticky="W")
website_label = Label(text="Website:")
website_label.grid(row=2, column=0, sticky="W")
email_label = Label(text="Email/Username:")
email_label.grid(row=3, column=0, sticky="W")
password_label = Label(text="Password:")
password_label.grid(row=4, column=0, sticky="W")
# Entries
user_entry = Entry()
user_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
user_entry.focus()
website_entry = Entry()
website_entry.grid(row=2, column=1, sticky="EW")
email_entry = Entry()
email_entry.grid(row=3, column=1, columnspan=2, sticky="EW")
password_entry = Entry()
password_entry.grid(row=4, column=1, sticky="EW")
# Buttons
search_button = Button(text="Search", command=search_details)
search_button.grid(row=2, column=2, sticky="EW")
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=2, sticky="EW")
add_button = Button(text="Add", width=21, command=add_password)
add_button.grid(row=5, column=1, sticky="W")
delete_button = Button(text="Delete", width=21, command=delete_entry)
delete_button.grid(row=5, column=2, sticky="W")
new_user_button = Button(text="NEW USER", width=50, command=new_user)
new_user_button.grid(row=6, column=1, columnspan=2, sticky="EW")
window.mainloop()
