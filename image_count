#!/usr/bin/env python

import Tkinter as tk
from PIL import ImageTk, Image
import argparse

parser = argparse.ArgumentParser(description='Display an image with counter.')
parser.add_argument('image')
parser.add_argument('--max_width', type=float, default=800.0, help="Maximum width to display.")
parser.add_argument('--max_height', type=float, default=600.0, help="Maximum height to display.")
parser.add_argument('--font_size', type=int, default=100, help="Font size for counter.")
args = parser.parse_args()

window = tk.Tk()
window.title("ImageCount " + args.image)

image = Image.open(args.image)

width_ratio = image.width / args.max_width
height_ratio = image.height / args.max_height
max_ratio = max(width_ratio, height_ratio)

if max_ratio > 1.0:
    new_width = int(image.width / max_ratio)
    new_height = int(image.height / max_ratio)
    image = image.resize((new_width, new_height), Image.ANTIALIAS)

image = ImageTk.PhotoImage(image)

count = tk.IntVar()
count_panel = tk.Label(window, textvariable=count, font=("Helvetica", args.font_size))
count_panel.pack()

image_panel = tk.Label(window, image=image)
image_panel.pack()

increment = lambda event: count.set(count.get()+1)
decrement = lambda event: count.set(count.get()-1)

window.bind("<Up>", increment)
window.bind("<Right>", increment)
window.bind("<Down>", decrement)
window.bind("<Left>", decrement)
window.mainloop()
