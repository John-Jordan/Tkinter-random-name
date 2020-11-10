import random
from tkinter import *   
from tkinter import ttk
from tkinter import messagebox
root = Tk()



def retrieve_input():
    input = text.get('1.0', END)
    names = input.split('\n')
    names = list(filter(lambda line: len(line) > 0, names))
    winner = random.choice(names)
    print(winner)

#names = list(filter(lambda line: len(line) > 0, text.get('0.0', END).split('\n')))

label = ttk.Label(root, text = "Random Name Selector")
label.pack()
label.config(font = ("serif", 25, 'bold'))
label.config(foreground = '#64b1bc', background = '#622ab8')
logo = PhotoImage(file = 'neora-LOGO.ppm')
new_logo = logo.subsample(7, 7)
label.config(image = new_logo)
label.config(compound = 'left')

enter_name = ttk.Label(root, text = 'Enter names for drawing on individual lines: ')
enter_name.pack()
text = Text(root, width = 40, height = 20)
text.pack()

button = ttk.Button(root, text = 'Choose Winner', command = retrieve_input)
button.pack()


root.mainloop()
