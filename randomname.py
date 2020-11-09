import random
from tkinter import *   
from tkinter import ttk
root = Tk()

label = ttk.Label(root, text = "Random Name Selector")
label.pack()
label.config(font = ("serif", 25, 'bold'))
label.config(foreground = '#64b1bc', background = '#622ab8')
logo = PhotoImage(file = 'neora-LOGO.ppm')
new_logo = logo.subsample(7, 7)
label.config(image = new_logo)
label.config(compound = 'left')

enter_name = ttk.Label(root, text = 'Add name to drawing: ')
enter_name.pack(side = 'left')
entry = ttk.Entry(root, width = 24)
entry.pack(side = 'left')




names = ['Billy Ray', 'Bobby Sue', 'Aunti Em', 'Crocodile Dundee', 'David Hasselhoff']

winner = random.choice(names)
print(f'The winner is {winner}!!!! Congratulations!')




root.mainloop()
