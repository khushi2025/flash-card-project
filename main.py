from tkinter import *
import pandas
import random

from tkinter import messagebox
BACKGROUND_COLOR = "#B1DDC6"
current_card={}
data_todict={}
def word_change():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(data_todict)
    canvas.itemconfigure(title,text="French",fill="#000000")
    canvas.itemconfigure(word,text=current_card["French"],fill="#000000")
    canvas.itemconfigure(image, image=image1)
    flip_timer=window.after(3000,func= flash)
def flash():
  canvas.itemconfigure(title,text="English",fill="#FFFFFF")
  canvas.itemconfigure(word,text=current_card["English"],fill="#FFFFFF")
  canvas.itemconfigure(image,image=image2)
def is_known():
    data_todict.remove(current_card)
    word_change()
    data=pandas.DataFrame(data_todict)
    data.to_csv("data/words_to_learn.csv",index=False)

window=Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
flip_timer=window.after(3000,func=flash)
try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    orginal_data=pandas.read_csv("data/french_words.csv")
    data_todict=orginal_data.to_dict(orient="records")
else:
    data_todict=data.to_dict(orient="records")
image1=PhotoImage(file="images/card_front.png")
cross_img=PhotoImage(file="images/wrong.png")
check_img=PhotoImage(file="images/right.png")
image2=PhotoImage(file="images/card_back.png")

canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
image=canvas.create_image(400,263,image=image1)
title=canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
word=canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)
unknown=Button(image=cross_img,highlightthickness=0,command=word_change)
unknown.grid(rows=1,column=0)
known=Button(image=check_img,highlightthickness=0,command=is_known)
known.grid(row=1,column=1)
word_change()

window.mainloop()

