import tkinter as tk
from tkinter import messagebox, filedialog
import os
from PIL import ImageTk, Image 

from board_panel import BoardPanel
from board_panel_image import BoardPanelImage
from game import Game
from new_game_dialog import NewGameDialog

def divide_img(image, cols, rows):
    result = []
    result.append(None) #0 means empty square
    w, h = image.size
    row_size = int(h / rows)
    col_size = int(w / cols)
    for row in range(rows):
        top = row * row_size
        bottom = top + row_size
        for col in range (cols):
            left = col * col_size
            right = left + col_size
            result.append(image.crop([left, top, right, bottom]))
    result.pop()    #last square should be empty
    return result
            

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
        self.image = None
        self.photo = None
        self.square_photos = None

        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        menu.add_command(label='Shuffle', command=self.shuffle)
        menu.add_command(label='Start', command=self.start)
        menu.add_command(label='Open picture', command=self.open_picture)

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
        self.image = None
        self.photo = None
        self.game = Game(w, h)
        self.game.shuffle()
        if self.board: self.board.destroy()
        self.board = BoardPanel(self.root, w, h, width=400, height=400, bg="black")
        self.board.add_listener(self)
        self.board.pack()
        self.board.draw_game_state(self.game)
        self.root.title("Sliding Puzzle")

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
            if self.image:
                self.board.delete("all")
                self.board.create_image(int(self.photo.width() / 2), int(self.photo.height() / 2), image=self.photo)

    def shuffle(self):
        """Shuffle the squares of `game` randomly, show the new game state in `board`.
        """
        self.game.shuffle()
        self.root.title("Sliding Puzzle")
        self.board.draw_game_state(self.game)
    
    def open_picture(self):
        self.image = None
        ftypes = [('JPEG files', '*.jpg')]
        filename = filedialog.askopenfilename(initialdir = os.curdir,title = "Select file",filetypes = ftypes)
        self.image = Image.open(filename)
        self.photo = ImageTk.PhotoImage(self.image)
        if self.image:
            NewGameDialog(self.root, self.new_game_image)
    
    def new_game_image(self, w, h):
        """Starts a new game with w x h board with self.image instead of numbers.

        Params:
            w (int): Width of the board in squares.
            h (int): Height of the board in squares.
        """
        if not self.image: return
        square_imgs = divide_img(self.image, w, h)
        self.square_photos = [None]
        self.square_photos.extend([ImageTk.PhotoImage(img) for img in square_imgs[1:]])
        self.game = Game(w, h)
        self.game.shuffle()
        if self.board: self.board.destroy()
        w_px = self.square_photos[1].width() * w
        h_px = self.square_photos[1].height() * h
        self.board = BoardPanelImage(self.root, w, h, self.square_photos, width=w_px, height=h_px, bg="black")
        self.board.add_listener(self)
        self.board.pack()
        self.board.draw_game_state(self.game)
        self.root.title("Sliding Puzzle")

main = Main()
