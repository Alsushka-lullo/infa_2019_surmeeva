from tkinter import *

list_of_names = []
for i in range(0, len(list_of_names), 2):
    list_of_names[i].grid(row=i, column=1)
    list_of_names[i+1].grid(row=i, column=2)

mainloop()
