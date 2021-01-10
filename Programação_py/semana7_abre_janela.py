# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 15:53:18 2020

@author: Andre

#classe Tk
#from tkinter import Tk
#criar objeto root
#root = Tk()
#chamada ao metodo mainloop
#root.mainloop()

#Adicionando funcionalidades a janela como text
#from tkinter import Tk, Label
#root = Tk()
#hello = Label(master = root, text = 'Ola classe')
#hello.pack()
#root.mainloop()


#adicionando imagem
"""
from tkinter import Tk, Label, PhotoImage
root = Tk()

photo = PhotoImage(file='logo.gif').subsample(2)
hello = Label(master=root, image=photo, width=300, height=180)
hello.pack()
root.mainloop()