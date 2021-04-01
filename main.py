import tkinter as tk
from tkinter import messagebox
from board_panel import BoardPanel
from game import Game

class Main:
    def __init__(self, game, board, root):
        self.game = game
        self.board = board
        self.root = root

    def click(self, x, y):
        if game.is_solved(): return
        self.game.press(x, y)
        #print(self.game)
        self.board.draw_game_state(self.game)
        if game.is_solved():
            #tk.messagebox.showinfo(message='SOLVED!')
            root.title("SOLVED!")

root = tk.Tk()
root.title("Sliding Puzzle")
game = Game(4, 4)
game.shuffle()
board = BoardPanel(root, 4, 4, width=400, height=400, bg="black")


main = Main(game, board, root)
board.add_listener(main)
board.pack()
board.draw_game_state(game)
board.mainloop()
