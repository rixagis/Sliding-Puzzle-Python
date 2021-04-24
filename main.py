import tkinter as tk
from tkinter import messagebox
from board_panel import BoardPanel
from game import Game
from new_game_dialog import NewGameDialog

class Main:
    """Utilitary class responsible for intercommunication between game, board_panel and tk root.

    Attributes:
        game (Game): Respective Game object.
        board (BoardPanel): Respective BoardPanel object.
        root: board's tk root object.
    """

    def __init__(self):
        """Initialize Main object.

        Args:
            game (Game): Respective Game object.
            board (BoardPanel): Respective BoardPanel object.
            root: board's tk root object.
        """
        self.game = None
        self.board = None
        self.root = tk.Tk()
        self.root.title("Sliding Puzzle")

        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        menu.add_command(label='Shuffle', command=self.shuffle)
        menu.add_command(label='Start', command=self.start)

        self.root.mainloop()
    
    def start(self):
        """Creates a dialog window asking for board params. That widndow must create new game"""
        
        NewGameDialog(self.root, self.new_game)
        

    def new_game(self, w, h):
        """Starts a new game with w x h board.

        Params:
            w (int): Width of the board in squares.
            h (int): Height of the board in squares.
        """
        self.game = Game(w, h)
        self.game.shuffle()
        if self.board: self.board.destroy()
        self.board = BoardPanel(self.root, w, h, width=400, height=400, bg="black")
        self.board.add_listener(self)
        self.board.pack()
        self.board.draw_game_state(self.game)

    def click(self, x, y):
        """Process mouse click event. Interface for `board` object.

        Args:
            x (int): x coord of click, in squares.
            y (int): y coord of click, in squares.
        """
        if self.game.is_solved(): return
        self.game.press(x, y)
        self.board.draw_game_state(self.game)
        if self.game.is_solved():
            self.root.title("SOLVED!")

    def shuffle(self):
        """Shuffle the squares of `game` randomly, show the new game state in `board`.
        """
        self.game.shuffle()
        self.root.title("Sliding Puzzle")
        self.board.draw_game_state(self.game)

main = Main()
