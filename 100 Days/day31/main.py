from asyncore import read
from cgitb import text
from curses import window
from email.mime import image
from sqlite3 import PARSE_DECLTYPES
from textwrap import fill
from  tkinter import *
from turtle import Screen, bgcolor
from webbrowser import BackgroundBrowser
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("100-Days-Of-Code/100 Days/day31/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("100-Days-Of-Code/100 Days/day31/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image = front_pic)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image= back_pic)

def is_right():
    to_learn.remove(current_card)

    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv")
    next_card()


#UI Part
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)



canvas = Canvas(width=800, height=526)
front_pic = PhotoImage(file="100-Days-Of-Code/100 Days/day31/images/card_front.png")
back_pic = PhotoImage(file="100-Days-Of-Code/100 Days/day31/images/card_back.png")
card_background = canvas.create_image(400,263, image = front_pic)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 30, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 50, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

cross_pic = PhotoImage(file="100-Days-Of-Code/100 Days/day31/images/wrong.png")
cross_button = Button(image=cross_pic, highlightthickness=0, command=next_card)
cross_button.grid(column=0, row=1)


checkmark_pic = PhotoImage(file="100-Days-Of-Code/100 Days/day31/images/right.png")
checkmark_button = Button(image=checkmark_pic, highlightthickness=0, command=is_right)
checkmark_button.grid(column=1, row=1)


next_card()



window.mainloop()