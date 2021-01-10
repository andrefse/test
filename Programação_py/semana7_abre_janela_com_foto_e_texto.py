# -*- coding: utf-8 -*-

from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM
root = Tk()

photo = PhotoImage(file='logo.gif').subsample(2)
image = Label(master=root, image=photo)
image.pack(side=TOP)
text = Label(master=root, font=("courier", 18), text="Olá alunos!!")
text.pack(side=BOTTOM)
root.mainloop()