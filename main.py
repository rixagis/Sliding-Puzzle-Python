import tkinter as tk
from tkinter import messagebox
from board_panel import BoardPanel
from game import Game

root = tk.Tk()

game = Game(4, 4)
game.shuffle()
board = BoardPanel(root, 4, 4, width=400, height=400, bg="black")

#print(game)

class Main:
    def __init__(self, game, board):
        self.game = game
        self.board = board

    def click(self, x, y):
        #print('clicked: %s, %s' % (x, y))
        self.game.press(x, y)
        #print(self.game)
        self.board.draw_game_state(self.game)
        if game.is_solved():
            tk.messagebox.showinfo(message='SOLVED!')

main = Main(game, board)
board.add_listener(main)
board.pack()
board.draw_game_state(game)
board.mainloop()
