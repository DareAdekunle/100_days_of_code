import tkinter as tk

window = tk.Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)

# create a label
my_label = tk.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

def clicked_button():
    print("Button was clicked")
    my_label["text"] = input.get()

input = tk.Entry(width=10)
 

button = tk.Button(text="click me", command=clicked_button)
button.pack()

input.pack()
print(input.get())




window.mainloop()  