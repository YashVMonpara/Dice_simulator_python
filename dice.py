import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import random

win = tk.Tk()
win.title('Random dice number generator')
win.geometry('305x330')


def show_dice():
    # Generate random number
    num = random.randint(1, 6)

    # Show dice images based on random number
    load = Image.open(f"dice{num}.png")

    # Resizing the image
    load = load.resize((300, 300), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)

    dice = tk.Label(win, image=render)
    dice.image = render
    dice.grid(row=0, column=0)


btn = ttk.Button(win, text='Roll the Dice', command=show_dice)
btn.grid(row=1, column=0)

win.mainloop()
