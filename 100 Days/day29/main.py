from tkinter import *
from tkinter import messagebox
from turtle import title
from random import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_btn():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in  range(randint(4, 6))]
    password_symbols = [choice(symbols) for _ in  range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in  range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    pass_input.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    popup_message = messagebox.showinfo(title="Invalid entry", message="Please don't leave any fields empty")
    website = website_input.get()
    email = email_input.get()
    password = pass_input.get()


    if len(website) == 0 or len(password) == 0:
        popup_message
    else:
        is_ok = messagebox.askokcancel(title= website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("100-Days-Of-Code/100 Days/day29/data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                email_input.delete(0, END)
                pass_input.delete(0, END)


    

# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("MyPass")
window.config(padx=20,pady=20)

logo_pic = PhotoImage(file="100-Days-Of-Code/100 Days/day29/logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100,100, image=logo_pic)
canvas.grid(column=1, row=0)

website_lbl = Label(text="Website:")
website_lbl.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_lbl = Label(text="Email/Username: ")
email_lbl.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "rebecca@email.com")

pass_lbl=Label(text="Password:")
pass_lbl.grid(column=0, row=3)

pass_input = Entry(width=20)
pass_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", width=15, command=generate_btn)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row = 4, columnspan=2)

window.mainloop()