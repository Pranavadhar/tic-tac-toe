import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Initialize variables
current_player = "X"
game_over = False
moves = 0

# Create buttons
buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(root, text="", width=10, height=5)
        button.grid(row=i, column=j)
        button.config(command=lambda button=button: process_move(button))
        row.append(button)
    buttons.append(row)


# Function to process a move
def process_move(button):
    global current_player, game_over, moves

    if button["text"] == "" and not game_over:
        button["text"] = current_player
        moves += 1

        if check_winner(current_player):
            messagebox.showinfo("Game Over", "Player " + current_player + " wins!")
            game_over = True
            root.quit()
        elif moves == 9:
            messagebox.showinfo("Game Over", "It's a tie!")
            game_over = True
            root.quit()
        else:
            current_player = "O" if current_player == "X" else "X"


# Function to check if a player has won
def check_winner(player):
    for i in range(3):
        if (
            buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] == player
            or buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] == player
        ):
            return True

    if (
        buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] == player
        or buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] == player
    ):
        return True

    return False


# Run the game
root.mainloop()
