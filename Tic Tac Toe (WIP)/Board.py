# Board.py
# Represent the game board using tkinter
import tkinter as tk
from tkinter import font

FONT = ("Ariel", 32)

class Board:
    def __init__(self, player):
        # Create the game board
        self.board = [["" for j in range(3)] for i in range(3)]
        self.buttons = [[None for j in range(3)] for i in range(3)]

        # Create the root window
        self.root = tk.Tk()
        self.root.title("TicTacToe")
        self.root.geometry("345x550")   

        # Create the main frame for the game
        self.content = tk.Frame(self.root)
        self.content.grid(sticky="NSEW")
        self.configure_frame(self.content, 1, 5, 4)

        # Create the display for the game
        self.text = tk.StringVar()
        self.display = tk.Label(self.content, textvariable=self.text, height=2, width=20, font=('Ariel', 24), bg='White', relief="ridge", bd=4)
        self.display.grid(column=0, columnspan=3, row=3, pady=10)


        # Reset button
        self.reset_button = tk.Button(self.content, font=("Ariel", 18), text="Reset", height=2, width=10, relief='groove')
        self.reset_button.grid(column=0, columnspan=3, row=4)

        # Generate a 3x3 grid
        self.grid_generator(3, 3, 3)

        # Run the gui
        self.root.mainloop()

    def grid_generator(self, size, columns, rows):
        # Generate buttons for the tic-tac-toe grid
        for col in range(columns):
            for row in range(rows):
                button = tk.Button(self.content, bg='Grey', text="", font=FONT, width=size+2, height=size, command=lambda col=col, row=row: self.on_click(row, col, self.player))
                button.grid(column=col, row=row, sticky="NSEW", padx=2, pady=2)
                self.buttons[row][col] = button
                
    def configure_frame(self, frame, weight, rows, columns):
        # Style the main frame's structure
        for i in range(rows):
            frame.rowconfigure(i, weight=weight)
        for i in range(columns):
            frame.columnconfigure(i, weight=weight)

    def on_click(self, row, col, player):
        # Update the button's shape(X/O) upon being clicked
        if self.board[row][col] == "":
            self.board[row][col] = player
            self.buttons[row][col].configure(text=player)
