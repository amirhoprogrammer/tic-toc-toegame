import tkinter as tk 
import random
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root, mode):
        self.root = root#make a page of game
        self.root.title("Tic-Tac-Toe")
        self.root.config(bg="black")

        self.mode = mode#for determination of userturn

        self.player_scores = {"X": 0, "O": 0}  # Initialize player scores
        self.current_player = "X"#default
        self.board = [" " for _ in range(9)]

        self.score_labels = {}
        for player in self.player_scores:#show the scores
            label = tk.Label(root, text=f"{player} {self.player_scores[player]}", font=("Helvetica", 14),bg="black",fg="green")
            label.grid(row=0, column=len(self.score_labels), padx=10, pady=5)
            self.score_labels[player] = label

        self.buttons = []
        for i in range(9):#show the board of game
            row, col = divmod(i, 3)
            button = tk.Button(root, text=" ", font=("Helvetica", 24), width=5, height=2,
                               command=lambda i=i: self.on_click(i),bg="black",fg="green")
            button.grid(row=row + 1, column=col)
            self.buttons.append(button)

        if self.mode == "computer" and self.current_player == "O":#computer plays 
            self.computer_move()

    def on_click(self, index):
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player,fg = "red" if self.current_player=="X" else "blue")
            if self.check_winner():
                self.player_scores[self.current_player] += 1  # Increment score of the winning player
                self.update_score_labels()  # Update score labels
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!\nScores:\n X = {self.player_scores['X']},\n O = {self.player_scores['O']}")
                self.reset_game()#show the result
            elif " " not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")#show the result
                self.reset_game()
            else:#determination the computer turn
                self.current_player = "X" if self.current_player == "O" else "O"
                if self.mode == "computer" and self.current_player == "O":
                    self.computer_move()
                                    
    def check_winner(self):
        win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]

        for pattern in win_patterns:
            if self.board[pattern[0]] == self.board[pattern[1]] == self.board[pattern[2]] != " ":
                return True
        return False

    def reset_game(self):#if game end it will restart the game 
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ")
        self.current_player = "X"

    def update_score_labels(self):#if anyone wins One point will added to her score 
        for player, label in self.score_labels.items():
            label.config(text=f"{player} {self.player_scores[player]}")

    def computer_move(self):
        empty_cells = [i for i, cell in enumerate(self.board) if cell == " "] #make a empty cells for game
        if empty_cells:
            # Check for potential winning moves
            for index in empty_cells:
                self.board[index] = "O"
                if self.check_winner():
                    self.buttons[index].config(text="O", fg = "red" if self.current_player=="X" else "blue")
                    self.player_scores[self.current_player] += 1  # Increment score of the winning player
                    self.update_score_labels()  # Update score labels
                    messagebox.showinfo("Game Over", f"Player {self.current_player} wins!\nScores:\n X = {self.player_scores['X']}\n O = {self.player_scores['O']}")
                    self.reset_game()
                    return
                self.board[index] = " "

            # Check for blocking opponent's winning moves
            for index in empty_cells:
                self.board[index] = "X"
                if self.check_winner():
                    self.board[index] = "O"
                    self.buttons[index].config(text="O", fg = "red" if self.current_player=="X" else "blue")
                    self.current_player = "X"
                    return
                self.board[index] = " "

            # If no winning or blocking moves, choose a random empty cell
            move_index = random.choice(empty_cells)
            self.board[move_index] = "O"
            self.buttons[move_index].config(text="O", fg = "red" if self.current_player=="X" else "blue")
            self.current_player = "X"
        else:#if noone doesn't win
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_game()

def start_game(mode):#if user push the button to start the game
    root = tk.Tk()
    game = TicTacToe(root, mode)
    root.mainloop()

def choose_mode(): #this page will load if you run this game
    mode_window = tk.Tk() 
    mode_window.title("Choose Mode") #title
    mode_window.config(bg="black") #background of page
    
   
    def start_two_player(): #if user click on two player
        mode_window.destroy()
        start_game("two_player")

    def start_vs_computer(): #if user click on vs computer
        mode_window.destroy()
        start_game("computer")

    
    tk.Label(mode_window, text="Choose mode:", font=("Helvetica", 16),bg="black",fg="green",padx=20,pady=10).grid(row=0,column=1)
    tk.Button(mode_window, text="Two Player", font=("Helvetica", 14), command=start_two_player ,width="15",fg="green",bg="black").grid(row=1,column=2)
    tk.Button(mode_window, text="Vs Computer", font=("Helvetica", 14), command=start_vs_computer ,width="15",fg="green",bg="black").grid(row=2,column=2)
    tk.Label(mode_window,bg="black",padx=30).grid(row=3,column=3) #make a space
    #tk.Label(mode_window,bg="black").grid(row=1,column=4) #make a space
    

    mode_window.mainloop()

if __name__ == "__main__": #run this game 
    choose_mode()