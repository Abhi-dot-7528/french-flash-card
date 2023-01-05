from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ----------------- Read Data -----------------
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

# ----------------- CHANGE CARD FUNCTIONALITY -----------------
current_card = {}


def next_card():
    """
    Randomly chooses a French word  and its Eng. translation in form of dict.
    Shows it onto the card.
    Flips card to its English word after 3 seconds.
    """
    global current_card, timer_card_flip
    window.after_cancel(timer_card_flip)
    current_card = random.choice(to_learn)
    canvas.itemconfig(current_card_bg, image=card_front_img)
    canvas.itemconfig(card_title_txt, text="French", fill="black")
    canvas.itemconfig(card_word_txt, text=current_card["French"], fill="black")
    timer_card_flip = window.after(3000, func=flip_card)


def flip_card():
    """
    Shows Flipped card with English translation of French word.
    """
    canvas.itemconfig(current_card_bg, image=card_back_img)
    canvas.itemconfig(card_title_txt, text="English", fill="white")
    canvas.itemconfig(card_word_txt, text=current_card["English"], fill="white")


# ----------------- UI SETUP -----------------
window = Tk()
window.title("Flash App")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)
canvas = Canvas(width=900, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)

# Update window after 3 seconds
timer_card_flip = window.after(3000, func=flip_card)

# Canvas Background
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
current_card_bg = canvas.create_image(450, 300, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

# Canvas Text
card_title_txt = canvas.create_text(450, 150, font=("Dancing Script", 40, "bold"))
card_word_txt = canvas.create_text(450, 300, font=("Comfortaa", 50))

# Button - Cross
red_cross_img = PhotoImage(file="./images/wrong.png")
dont_know_btn = Button(image=red_cross_img, borderwidth=0, highlightthickness=0, command=next_card)
dont_know_btn.grid(column=0, row=1)

# Button - Check
green_check_img = PhotoImage(file="./images/right.png")
know_btn = Button(image=green_check_img, borderwidth=0, highlightthickness=0, command=next_card)
know_btn.grid(column=1, row=1)

next_card()

window.mainloop()
