import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET --------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label["text"] = "Timer"
    counter_label.config(text="")

# ---------------------------- TIMER MECHANISM ----------------------------- # 
def start_countdown():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60 
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label['text'] = "break"
        timer_label['fg'] = RED
 
    elif reps % 2 == 0: 
        countdown(short_break_sec)
        timer_label['text'] = "break"
        timer_label['fg'] = PINK
    else:
        countdown(work_sec)
        timer_label['text'] = "Work"
        timer_label['fg'] = GREEN

# ---------------------------- COUNTDOWN MECHANISM ------------------------- # 
def countdown(start_num):
    global timer
    min = math.floor(start_num/60)
    sec = start_num%60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if start_num > 0:
        timer = window.after(1000, countdown, start_num - 1)
    else:
        start_countdown()
        check_reps = math.floor(reps/2)
        counter_label.config(text="✔"*check_reps)


# ---------------------------- UI SETUP ------------------------------------ #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas= tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", 
                                font=(FONT_NAME, 35,  "bold"))
canvas.grid(column=1, row=1)

timer_label = tk.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), 
                       bg=YELLOW, highlightthickness=0)
timer_label.grid(column=1, row=0)

start_button = tk.Button(text="Start", font=(FONT_NAME, 10, "bold"), 
                         command=start_countdown)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", font=(FONT_NAME, 10, "bold"), 
                         command=reset_timer)
reset_button.grid(column=2, row=2)

counter_label = tk.Label(text="", fg=GREEN, font=(FONT_NAME, 10, "bold"), 
                       bg=YELLOW, highlightthickness=0)
counter_label.grid(column=1, row=4)


window.mainloop()