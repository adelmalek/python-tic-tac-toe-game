from tkinter import *
import random

# *********
# FUNCTIONS
# *********

def next_turn(row, column):
    global player

    if board[row][column]["text"] == "" and check_winner() is False:
        if player == players[0]:
            board[row][column]["text"] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + " turn"))
            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))
            elif check_winner() is "Tie":
                label.config(text="Tie")
        else:
            board[row][column]["text"] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))
            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))
            elif check_winner() is "Tie":
                label.config(text="Tie")


def check_winner():
    for row in range(3):
        if board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] != "":
            board[row][0].config(bg="blue")
            board[row][1].config(bg="blue")
            board[row][2].config(bg="blue")
            return True

    for column in range(3):
        if board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] != "":
            board[0][column].config(bg="blue")
            board[1][column].config(bg="blue")
            board[2][column].config(bg="blue")
            return True

    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] != "":
        board[0][0].config(bg="blue")
        board[1][1].config(bg="blue")
        board[2][2].config(bg="blue")
        return True

    if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] != "":
        board[0][2].config(bg="blue")
        board[1][1].config(bg="blue")
        board[2][0].config(bg="blue")
        return True

    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                board[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False


def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if board[row][column]["text"] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game():
    global player

    player = random.choice(players)
    label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", bg="#F0F0F0")


# **********
# GAME BOARD
# **********

window = Tk()

players = ["Tom", "Jerry"]
player = random.choice(players)

label = Label(text=(player + " turn"), font=("consolas", 40))
label.pack()

restart_btn = Button(text="New Game", font=("consolas", 20), command=new_game)
restart_btn.pack()

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        board[row][column] = Button(frame,
                                    text="",
                                    font=("consolas", 40), 
                                    width=6, height=2, 
                                    command=lambda row=row, column=column : next_turn(row, column))
        board[row][column].grid(row=row, column=column)

window.mainloop()