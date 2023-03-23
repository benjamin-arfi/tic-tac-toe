from tkinter import *
root = Tk()
root.geometry("400x550")
root.title("Tic Tac Toe")

frame1 = Frame(root)
frame1.pack()
titleLabel = Label(frame1,text="Menu",font=("Arial",25),bg="green",width=18)
titleLabel.grid(row=0, column=0, columnspan=3)

frame2 = Frame(root)
frame2.pack()

def jeuia():
    import ia
def jeu1v1():
    import tictactoe
def jeuiadur():
    import iadur

# Création d'un bouton au sein du frame 
b1= Button(frame2,text= " 1 vs 1 ", width = 20 ,height = 2 , font=("Arial", 15), relief= RAISED,command=jeu1v1)
b1.grid(row=0,column=0)
b2= Button(frame2,text= " ia player simple ", width = 20 ,height = 2 , font=("Arial", 15), relief= RAISED,command=jeuia )
b2.grid(row=1,column=0)
b3= Button(frame2,text= " ia player compliquee ", width = 20 ,height = 2 , font=("Arial", 15), relief= RAISED,command=jeuiadur )
b3.grid(row=2,column=0)

root.mainloop()