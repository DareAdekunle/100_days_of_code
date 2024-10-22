import tkinter as tk
from tkinter import messagebox as mb


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
from random import randint, choice, shuffle
def password_gen():
    global password_input
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 
               'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = [choice(letters) for i in range(randint(8, 10))]
    nr_symbols = [choice(symbols) for i in range(randint(2, 4))]
    nr_numbers = [choice(numbers) for i in range(randint(2, 4))]

    password_list = nr_letters+nr_symbols+nr_numbers
    shuffle(password_list)
    password = "".join(password_list)

    password_input.delete(0, "end")
    password_input.insert(0, password)

    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def savePassword():

    global web_input, password_input, user_input 

    if len(web_input.get()) <1 or len( password_input.get()
                                      ) < 1 or len(user_input.get()) < 1:
        mb.showerror(title="Error", message="Please fill all required fields")


    else:
        ask2cancel = mb.askokcancel(
            message=f"Details are:\nWebsite: {web_input.get()}\
                \nEmail/Username: {user_input.get()}\
                \nPassword: {password_input.get()}")
        
        if ask2cancel:
            with open("password_file.txt", "a") as file:
                password_data = f"\nWebsite: {web_input.get()}\nEmail/Username: {user_input.get()}\nPassword: {password_input.get()}\n"
                file.write(password_data)

            web_input.delete(0, 'end')
            password_input.delete(0, 'end')
            user_input.delete(0, 'end')
            user_input.insert(0, "oludareadekunle@gmail.com")


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)



canvas= tk.Canvas(width=200, height=200, highlightthickness=0)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=0, row=0, columnspan=3)

web_label=tk.Label(text="Website:", font=("Arial", 10, "bold"))
web_label.grid(row=1, column=0)

web_input = tk.Entry(width=45)
web_input.focus()
web_input.grid(row=1, column=1, columnspan=2)

user_label = tk.Label(text="Email/Username:", font=("Arial", 10, "bold"))
user_label.grid(row=2, column=0)

user_input = tk.Entry(width=45)
user_input.grid(row=2, column=1, columnspan=2)
user_input.insert(0, "oludareadekunle@gmail.com")

password_label = tk.Label(text="Password:", font=("Arial", 10, "bold"))
password_label.grid(row=3, column=0, columnspan=1)

password_input = tk.Entry(width=21)
password_input.grid(row=3, column=1, columnspan=1)

password_button = tk.Button(text="Generate Password", font=("Arial", 10), 
                            command=password_gen)
password_button.grid(row=3, column=2, columnspan=1)


add_button = tk.Button(text="Add", width=40, command=savePassword)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()