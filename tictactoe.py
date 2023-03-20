from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Tic Tac Toe")

frame1 = Frame(root)
frame1.pack()
titleLabel = Label(frame1,text="Tic Tac Toe",font=("Arial",25),bg="green")
titleLabel.pack()

frame2 = Frame(root)
frame2.pack()

board = {1:"  " , 2:"  " , 3:"  ",
         4:"  " , 5:"  " , 6:"  ",
         7:"  " , 8:"  " , 9:"  " }

turn = "x"
def win(player):
    #gagner en range
    if board[1] == board[2] and board[2] == board[3] and board[3]== player:
        return True
    elif board[4] == board[5] and board[5] == board[6] and board[6]== player:
        return True
    elif board[7] == board[8] and board[8] == board[9] and board[9]== player:
        return True
    #gagner en colone
    elif board[1] == board[4] and board[4] == board[7] and board[7]== player:
        return True
    elif board[2] == board[5] and board[5] == board[8] and board[8]== player:
        return True
    elif board[3] == board[6] and board[6] == board[9] and board[9]== player:
        return True
    #gagner en diagonales
    elif board[1] == board[5] and board[5] == board[9] and board[9]== player:
        return True
    elif board[3] == board[5] and board[5] == board[7] and board[7]== player:
        return True

    return False
def checkgame():
    for i in board.keys():
        if board [i] == "  ":
            return False
    return True
def play(event):
    global turn 
    button = event.widget
    buttontext = str(button)
    clicked = buttontext[-1]
    print(clicked)
    if clicked == "n":
        clicked = 1
    else:
        clicked = int(clicked)
    if button["text"] == "  ":
        if turn == "x":
            button["text"]= "X"
            board[clicked] = turn
            if win(turn) :
                winLabel = Label(frame2 , text=f"{turn} a gagne la partie",font=("Arial",20),bg="gray")
                winLabel.grid(row= 3 , column= 0 , columnspan= 3)
            turn = "o"
        else:
            button["text"] = "O"
            board[clicked] = turn
            if win(turn) :
                winLabel = Label(frame2 , text=f"{turn} a gagne la partie",font=("Arial",20), bg="gray")
                winLabel.grid(row= 3 , column= 0 , columnspan= 3)
            turn = "x"
        if checkgame():
            winLabel = Label(frame2 , text= "partie nulle" ,font=("Arial",20), bg="gray")
            winLabel.grid(row= 3 , column= 0 , columnspan= 3)
#premiere range

button1 = Button(frame2,text= "  ", width = 4 ,height = 2 , font=("Arial", 35), relief= RAISED )
button1.grid(row=0,column=0)
button1.bind("<Button-1>" , play)

button2 = Button(frame2,text= "  ", width = 4 ,height = 2 , font=("Arial", 35), relief= RAISED )
button2.grid(row=0,column=1)
button2.bind("<Button-1>" , play)

button3 = Button(frame2,text= "  ", width = 4 ,height = 2 , font=("Arial", 35), relief= RAISED )
button3.grid(row=0,column=2)
button3.bind("<Button-1>" , play)

#seconde rangee

button4 = Button(frame2,text= "  ", width = 4 ,height = 2 , font=("Arial", 35), relief= RAISED)
button4.grid(row=1,column=0)
button4.bind("<Button-1>" , play)

button5 = Button(frame2,text= "  ", width = 4 ,height = 2 , font=("Arial", 35), relief= RAISED)
button5.grid(row=1,column=1)
button5.bind("<Button-1>" , play)

button6 = Button(frame2,text= "  ", width = 4 ,height = 2 , font=("Arial", 35), relief= RAISED)
button6.grid(row=1,column=2)
button6.bind("<Button-1>" , play)

#troisieme rangee

button7 = Button(frame2,text = "  ", width = 4 ,height = 2 , font=("Arial", 35), relief= RAISED )
button7.grid(row=2,column=0)
button7.bind("<Button-1>" , play)

button8 = Button(frame2,text= "  ", width = 4 ,height = 2 , font=("Arial", 35), relief= RAISED )
button8.grid(row=2,column=1)
button8.bind("<Button-1>" , play)

button9 = Button(frame2,text= "  ", width = 4 ,height = 2 , font=("Arial", 35), relief= RAISED )
button9.grid(row=2,column=2)
button9.bind("<Button-1>" , play)

root.mainloop()