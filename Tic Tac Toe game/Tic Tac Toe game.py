from tkinter import *
import random

def next_turn(row, column):
    global player

    # Ensure the button is empty and there's no winner yet
    if buttons[row][column]["text"] == "" and determine_winner() is False:
        # Set the current player's move
        buttons[row][column]["text"] = player

        if determine_winner() is False:
            # Switch players
            if player == player1:
                player = player2 
            else:
                player = player1

            label.config(text=player)
        elif determine_winner() == "Tie":
            label.config(text="Tie!")
        else:
            label.config(text=f"{player} WINNER!")

def determine_winner():
    
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif available_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    return False

def available_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    return spaces > 0

def start_new_game():
    global player
    # Reset the board and randomize the starting player
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="lightblue")
    player = random.choice([player1, player2])
    label.config(text=player)


window = Tk()
window.title("Tic-Tac-Toe")


player1 = "X"
player2 = "O"
player = random.choice([player1, player2])  # Randomize who starts
buttons = [[0, 0, 0], 
           [0, 0, 0], 
           [0, 0, 0]]

label = Label(text=player, font=('Arial', 35))
label.pack(side="top")

reset_button = Button(text="Restart!", font=("Arial", 20), width=19, bg="green", fg="white", command=start_new_game)
reset_button.pack(side="bottom")

frame = Frame(window)
frame.pack()

# Create the game buttons
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=("Arial", 20), bg="lightblue", fg="red",
                                      height=3, width=6, command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
