from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


# ----------------- UI SETUP -----------------
window = Tk()
window.title("Flash App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=900, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)

# Canvas Background
card_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(450, 300, image=card_img)
canvas.grid(column=0, row=0, columnspan=2)

# Canvas Text
canvas.create_text(450, 150, text="Title", font=("Dancing Script", 40, "bold"))
canvas.create_text(450, 300, text="Word", font=("Comfortaa", 50))

# Button - Cross
red_cross_img = PhotoImage(file="./images/wrong.png")
dont_know_btn = Button(image=red_cross_img, borderwidth=0, highlightthickness=0)
dont_know_btn.grid(column=0, row=1)

# Button - Check
green_check_img = PhotoImage(file="./images/right.png")
know_btn = Button(image=green_check_img, borderwidth=0, highlightthickness=0)
know_btn.grid(column=1, row=1)

window.mainloop()
