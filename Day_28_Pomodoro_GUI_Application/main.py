from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer",fg=GREEN,bg=YELLOW)
    check_mark.config(fg=GREEN,bg=YELLOW)
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def count_down(count):
    count_min=count//60
    count_sec=count%60

    canvas.itemconfig(timer_text,text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        global timer
        timer=window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark=" "
        for _ in range(reps//2):
            mark+="✓"
        check_mark.config(text="mark",fg=GREEN,bg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps%8==0:
        count_down(long_break_sec)
        timer_label.config(text="Break",fg=RED,bg=YELLOW)
    elif reps %2==0:
        count_down(short_break_sec)
        timer_label.config(text="Break",fg=PINK,bg=YELLOW)
    else:
        count_down(work_sec)
        timer_label.config(text="Work",fg=GREEN,bg=YELLOW)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100,bg=YELLOW)


canvas = Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=photo)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=FONT_NAME)
canvas.grid(row=1,column=1)



timer_label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,30))
timer_label.grid(row=0,column=1)

check_mark=Label(font=(FONT_NAME,20),fg=GREEN,bg=YELLOW)
check_mark.grid(row=3,column=1)

start_button = Button(text="Start",font=FONT_NAME,command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset",font=FONT_NAME,command=reset_timer)
reset_button.grid(row=2,column=2)


window.mainloop()