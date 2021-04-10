import tkinter as tk
from tkinter import messagebox
from board_panel import BoardPanel
from game import Game

class Main:
    """Utilitary class responsible for intercommunication between game, board_panel and tk root.

    Attributes:
        game (Game): Respective Game object.
        board (BoardPanel): Respective BoardPanel object.
        root: board's tk root object.
    """

    def __init__(self, game, board, root):
        """Initialize Main object.

        Args:
            game (Game): Respective Game object.
            board (BoardPanel): Respective BoardPanel object.
            root: board's tk root object.
        """
        self.game = game
        self.board = board
        self.root = root

    def click(self, x, y):
        """Process mouse click event. Interface for `board` object.

        Args:
            x (int): x coord of click, in squares.
            y (int): y coord of click, in squares.
        """
        if game.is_solved(): return
        self.game.press(x, y)
        self.board.draw_game_state(self.game)
        if game.is_solved():
            root.title("SOLVED!")

    def shuffle(self):
        """Shuffle the squares of `game` randomly, show the new game state in `board`.
        """
        self.game.shuffle()
        root.title("Sliding Puzzle")
        self.board.draw_game_state(self.game)

root = tk.Tk()
root.title("Sliding Puzzle")
game = Game(4, 4)
game.shuffle()
board = BoardPanel(root, 4, 4, width=400, height=400, bg="black")

menu = tk.Menu(root)
root.config(menu=menu)


main = Main(game, board, root)
menu.add_command(label='Shuffle', command=main.shuffle)
board.add_listener(main)
board.pack()
board.draw_game_state(game)
board.mainloop()
