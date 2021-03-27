"""
This module contains class BoardPanel - a GUI element for showing game board.


"""

import tkinter

class BoardPanel(tkinter.Canvas):
    """
    UI element used to show the state of the board.

    Attributes:
        event_listener: Object listening for click events.
            Must provide 'click(x_cell, y_cell)' method.
        width_cells (int): Width of the board in cells.
        height_cells (int): Height of the board in cells.
        cell_width (int): Width of one cell in pixels.
        cell_height (int): Height of one cell in pixels.
    """

    def __init__(self, root, width_cells, height_cells, **kwargs):
        """Initializes a BoardPanel object.

        Args:
            root: tk root.
            width_cells (int): Width of the board in cells.
            height_cells (int): Height of the board in cells.
            **kwargs: tkinter canvas kwargs.
        """
        tkinter.Canvas.__init__(self, root, **kwargs)
        self.event_listener = None
        self.bind("<Button-1>", self.on_click)

        print(self["width"], self["height"])
        self.width_cells = width_cells
        self.cell_width = int(int(self["width"]) / self.width_cells)
        self.height_cells = height_cells
        self.cell_height = int(int(self["height"]) / self.height_cells)
    
    def add_listener(self, listener):
        """Adds event listener to the board.

        Args:
            listener: Object listening for click events.
                Must provide 'click(x_cell, y_cell)' method.
        """
        self.event_listener = listener

    def on_click(self, event):
        """Processes canvas mouse click event and dispatches to listener.
        """
        x_cell = int(event.x / self.cell_width)
        y_cell = int(event.y / self.cell_height)

        if self.event_listener:
            self.event_listener.click(x_cell, y_cell)

    def draw_game_state(self, game):
        """Displays the state of the game in canvas.

        Args:
            game (Game): Game object which state should be diplayed.
        """
        self.delete("all")

        for row in range(game.height):
            y = row * self.cell_height
            for column in range(game.width):
                x = column * self.cell_height
                number = game.get(column, row)
                if number != 0:
                    self.create_rectangle(x, y, x + self.cell_width, y + self.cell_height, fill='red')
                    self.create_text(x + int(self.cell_width) / 2, y + int(self.cell_height) / 2,
                        text=str(number), font=('arial', int(self.cell_height / 2)), fill='white')

    
