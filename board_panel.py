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

    def __init__(self, root, event_listener, width_cells, height_cells, **kwargs):
        """Initializes a BoardPanel object.

        Args:
            root: tk root.
            event_listener: Object listening for click events.
                Must provide 'click(x_cell, y_cell)' method.
            width_cells (int): Width of the board in cells.
            height_cells (int): Height of the board in cells.
            **kwargs: tkinter canvas kwargs.
        """
        tkinter.Canvas.__init__(root, **kwargs)
        self.event_listener = event_listener
        self.bind("<Button-1>", self.on_click)

        self.width_cells = width_cells
        self.cell_width = int(self.winfo_width() / self.width_cells)
        self.height_cells = height_cells
        self.cell_height = int(self.winfo_height() / self.height_cells)

    def on_click(self, event):
        """Processes canvas mouse click event and dispatches to listener.
        """
        x_cell = int(event.x / self.cell_width)
        y_cell = int(event.y / self.cell_height)

        self.event_listener.click(x_cell, y_cell)

    def draw_game_state(self, game):
        """Displays the state of the game in canvas.

        Args:
            game (Game): Game object which state should be diplayed.
        """
        self.delete("all")

        for row in game.height:
            y = row * self.cell_height
            for column in game.width:
                x = column * self.cell_height
                number = game.get(x, y)
                if number != 0:
                    self.create_rectangle(x, y, x + self.cell_width, self.cell_height, fill='red')
                    self.create_text(x + int(self.cell_width), y + int(self.cell_height), text=str(), fill='white')

    
