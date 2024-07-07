from tkinter import *
from tkinter import messagebox
import pandas
from random import choice
BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn = {}


try:
    # Reading csv file
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    # Returns a list of dictionaries
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    """Shows a random French word."""
    global current_card, flip_timer

    # Cancel the automatic call to flip_card function when ❌ or ✅ button is clicked to prevent the flipping of card.
    window.after_cancel(flip_timer)

    # Select a random word from to_learn dictionary
    current_card = choice(to_learn)

    # Setting up the canvas front when the ❌ or ✅ button is clicked.
    canvas.itemconfig(c_text_title, text="French", fill="black")
    canvas.itemconfig(c_text_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)

    # Automatically calls the flip_card function after 3 seconds
    flip_timer = window.after(3000, flip_card)


def flip_card():
    """Shows the English meaning of the French word."""
    # Setting up the canvas back
    canvas.itemconfig(c_text_title, text="English", fill="white")
    canvas.itemconfig(c_text_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back)


def is_known():
    """Remove the current word from French word dictionary(to_learn) if ✅ button clicked."""
    # Remove word from to_lean dictionary
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    # Creates a new file named 'words_to_learn.csv' that does not contain words known by the user
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------------------------UI SETUP-------------------------------------------------
# Creating tkinter window
window = Tk()
window.title("Flashy")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Automatically calls the flip_card function after 3 seconds
flip_timer = window.after(3000, flip_card)

# Creating canvas in window
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

# Reading images for the canvas foreground, background and buttons
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file=f"images/card_back.png")
image_wrong = PhotoImage(file="images/wrong.png")
image_right = PhotoImage(file="images/right.png")

# Setting up canvas front
canvas_image = canvas.create_image(400, 263, image=card_front)
c_text_title = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
c_text_word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Creating buttons
button_unknown = Button(image=image_wrong, highlightthickness=0, bg=BACKGROUND_COLOR, relief="flat", command=next_card)
button_known = Button(image=image_right, highlightthickness=0, bg=BACKGROUND_COLOR, relief="flat", command=is_known)
button_unknown.grid(row=1, column=0)
button_known.grid(row=1, column=1)

# Calling next_card function to generate the first French word.
next_card()

window.mainloop()



