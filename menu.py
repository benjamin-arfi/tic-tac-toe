from tkinter import *
from ia import *
from tictactoe import *


# Création d'un bouton au sein du frame 
button1= Button(frame2,text= " 1 vs 1 ", width = 20 ,height = 2 , font=("Arial", 15), relief= RAISED,)
button1.grid(row=0,column=0)
b2= Button(frame2,text= " ia player simple ", width = 20 ,height = 2 , font=("Arial", 15), relief= RAISED,command=jouer )
b2.grid(row=1,column=0)
b3= Button(frame2,text= " ia player compliquee ", width = 20 ,height = 2 , font=("Arial", 15), relief= RAISED )
b3.grid(row=2,column=0)
