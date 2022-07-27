# make tab screen
from tkinter import *
from tkinter import ttk

window = Tk()
window.iconbitmap('python.ico')

baseTab = ttk.Notebook(window)

tabDog = ttk.Frame(baseTab)
baseTab.add(tabDog, text = 'dog')
tabCat = ttk.Frame(baseTab)
baseTab.add(tabCat, text = 'cat')

baseTab.pack(expand = 1, fill = "both")

photoDog = PhotoImage(file = "gif/dog7.gif")
labelDog = Label(tabDog, image = photoDog)
labelDog.pack()

photoCat = PhotoImage(file = "gif/cat5.gif")
labelCat = Label(tabCat, image = photoCat)
labelCat.pack()

window.mainloop()