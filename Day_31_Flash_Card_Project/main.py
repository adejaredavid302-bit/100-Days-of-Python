
from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
try:
    data_file=pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("./data/french_words.csv")
    print(original_data)
    row = original_data.to_dict('records')
else:
    row=data_file.to_dict('records')


def next_cards():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(row)
    french_words=current_card["French"]
    canvas.itemconfig(card_title,text="French")
    canvas.itemconfig(card_word,text=french_words)
    canvas.itemconfig(card_background,image=card_front_image)
    flip_timer = window.after(3000,func=flip_cards)
def flip_cards():
    canvas.itemconfig(card_word,text="English",fill="white")
    english_words=current_card["English"]
    canvas.itemconfig(card_title,text=english_words)
    canvas.itemconfig(card_background,image=card_back_image)
def is_known():
    row.remove(current_card)
    data=pandas.DataFrame(row)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_cards()

window = Tk()
window.title("Flash Card Project")
window.configure(pady=50, padx=50, background=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip_cards)

canvas=Canvas(window,width=800,height=526)
card_front_image=PhotoImage(file="./images/card_front.png")
card_back_image=PhotoImage(file="./images/card_back.png")
card_background=canvas.create_image(400,263,image=card_front_image)
card_title=canvas.create_text(400,158,text="Title",font=("Times New Roman",18,"italic"))
card_word=canvas.create_text(400,260,text="BOYOY",font=("Times New Roman",18,"bold"))
canvas.configure(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=3,column=2,columnspan=2)

cross_image=PhotoImage(file="./images/wrong.png")
unknown_button=Button(image=cross_image,highlightthickness=0,command=next_cards)
unknown_button.grid(row=4,column=2)

check_image=PhotoImage(file="./images/right.png")
known_button=Button(image=check_image,highlightthickness=0,command=is_known)
known_button.grid(row=4,column=3)


next_cards()

window.mainloop()