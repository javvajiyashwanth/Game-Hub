import tkinter as tk
from tkinter import messagebox
import subprocess

class GameSelector(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Game Selector")
        self.geometry("150x90")

        self.ping_pong_button = tk.Button(self, text="Ping Pong", command=self.ping_pong)
        self.ping_pong_button.pack()

        self.tic_tac_toe_button = tk.Button(self, text="Tic-Tac-Toe", command=self.tic_tac_toe)
        self.tic_tac_toe_button.pack()

        self.snake_button = tk.Button(self, text="Snake", command=self.snake)
        self.snake_button.pack()

    def ping_pong(self):
        subprocess.call(["python3", "ping_pong.py"])

    def tic_tac_toe(self):
        subprocess.call(["python3", "tic_tac_toe.py"])

    def snake(self):
        subprocess.call(["python3", "snake.py"])


if __name__ == "__main__":
    game_selector = GameSelector()
    game_selector.mainloop()