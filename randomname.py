from tkinter import *   
from tkinter import ttk
root = Tk()

label = ttk.Label(root, text = "Random Name Selector")
label.pack()
label.config(font = ("Courier", 25, 'bold'))
label.config(foreground = '#64b1bc', background = 'white')
logo = PhotoImage(file = '/Users/johnjordan/Desktop/Python/Random/neora-LOGO.ppm')
new_logo = logo.subsample(7, 7)
label.config(image = new_logo)
label.config(compound = 'left')


root.mainloop()
