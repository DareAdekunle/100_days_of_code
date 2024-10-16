import tkinter as tk

window = tk.Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)

# create a label
my_label = tk.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

def clicked_button():
    print("Button was clicked")
    my_label["text"] = input.get()

input = tk.Entry(width=10)

button = tk.Button(text="click me", command=clicked_button)
button.grid(column=1, row=1)

input.grid(column=3, row=2)
print(input.get())

new_botton = tk.Button(text="New Button")
new_botton.grid(column=2, row=0)



window.mainloop()  