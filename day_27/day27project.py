import tkinter as tk

window = tk.Tk()
window.minsize(width=500, height=300)

px = 15
py= 5

def Miles2KmCalc():
    miles= input.get()
    km= float(miles)*1.60934
    label_c["text"] = round(km, 2)


input = tk.Entry()
input.grid(column=1, row=0)

label_a = tk.Label(text="Miles", font=("Arial", 24, "bold"))
label_a.grid(column=2, row=0, padx=px, pady=py)

label_b = tk.Label(text="is equal to", font=("Arial", 24, "bold"))
label_b.grid(column=0, row=1, padx=px, pady=py)

label_c = tk.Label(text="", font=("Arial", 24, "bold"))
label_c.grid(column=1, row=1, padx=px, pady=py)

label_d = tk.Label(text="Km", font=("Arial", 24, "bold"))
label_d.grid(column=2, row=1, padx=px, pady=py)

calc_button = tk.Button(text="Calculate", command=Miles2KmCalc)
calc_button.grid(column=1, row=2, padx=px, pady=py)



window.mainloop()