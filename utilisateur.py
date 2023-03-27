
from tkinter import *
root = Tk()
frame2 = Frame(root)
frame2.pack()

label_utilisateur = Label(frame2,text="utilisateur",font=("Arial",25),width=18)
label_utilisateur.grid(row=3,column=0)

entre_utilisateur = Entry(frame2)
entre_utilisateur.grid(row=4,column=0)

def C1():
    import menu
    

btn_ok = Button(frame2,text="entrez",font=("Arial",15),command=C1)
btn_ok.grid(row=5,column=0)

LF = LabelFrame(frame2,text="sortie")
LF.grid(row=6,column=1)
root.mainloop()