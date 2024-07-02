from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashy")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0 , bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
c_text_language = canvas.create_text(400, 150, text="French", fill= "black", font=("Ariel", 40, "italic"))
c_text_word = canvas.create_text(400, 263, text="histoire", fill= "black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

image_wrong = PhotoImage(file="images/wrong.png")
image_right = PhotoImage(file="images/right.png")
button_wrong = Button(image=image_wrong, highlightthickness=0, bg=BACKGROUND_COLOR, relief="flat")
button_right = Button(image=image_right, highlightthickness=0, bg=BACKGROUND_COLOR, relief="flat")
button_wrong.grid(row=1, column=0)
button_right.grid(row=1, column=1)


window.mainloop()
