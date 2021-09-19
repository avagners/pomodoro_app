from tkinter import *
import math
import winsound
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
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    window.after_cancel(timer)
    label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(text_timer, text='00:00')
    check_sym.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label.config(text='Break', fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label.config(text='Break', fg=PINK)
        count_down(short_break_sec)
    else:
        label.config(text='Work', fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(text_timer, text=f'{count_min}:{count_sec}')
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        winsound.PlaySound("bell-ringing-04.wav", winsound.SND_ASYNC)
        for _ in range(work_sessions):
            mark += '✔'
        check_sym.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro app')
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
text_timer = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 22, "bold"))
canvas.grid(column=1, row=1)

label = Label(text="Timer", font=(FONT_NAME, 42, "bold"), fg=GREEN, bg=YELLOW)
label.grid(column=1, row=0)

btn_start = Button(text='Start', relief=GROOVE, highlightthickness=0, command=start_timer)
btn_start.grid(column=0, row=2)

btn_reset = Button(text='Reset', relief=GROOVE, highlightthickness=0, command=reset_timer)
btn_reset.grid(column=2, row=2)

check_sym = Label(font=(FONT_NAME, 18, "bold"), fg=GREEN, bg=YELLOW)
check_sym.grid(column=1, row=3)

window.mainloop()
