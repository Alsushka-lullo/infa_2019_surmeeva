import tkinter
import operator

list_of_names = []  # this part gets and modifies information from the file
with open('Score.txt') as fp:
    line = fp.readline()
    while line:
        list_of_names.append(line)
        line = fp.readline()
dict_of_scores = {}
for i in range(0, len(list_of_names), 4):
    dict_of_scores[list_of_names[i].rstrip()] = float(list_of_names[i + 1]) / float(list_of_names[i + 2]) - \
                                                float(list_of_names[i + 3])  # creation of the dictionary
    # name-score in time
sorted_dict_of_scores = sorted(dict_of_scores.items(), key=operator.itemgetter(1))  # sorts this dictionary by value

root = tkinter.Tk()

tkinter.Label(text="Name of player").grid(row=0, column=0, padx=0, pady=10)  # creates the table with scores and names
tkinter.Label(text="Points in second").grid(row=0, column=1, padx=10, pady=10)
for j in range(len(sorted_dict_of_scores)):
    tkinter.Label(text=sorted_dict_of_scores[j][0]).grid(row=j + 1, column=0, padx=10, pady=10)
    tkinter.Label(text=sorted_dict_of_scores[j][1]).grid(row=j + 1, column=1, padx=10, pady=10)

root.mainloop()
