"""
This module contains class BoardPanel - a GUI element for showing game board.


"""

import tkinter

class BoardPanel(tkinter.Canvas):


    def __init__(self, root, event_listener, width_cells, height_cells, **kwargs):
        tkinter.Canvas.__init__(root, **kwargs)
        self.event_listener = event_listener
        self.bind("<Button-1>", self.on_click)

        self.width_cells = width_cells
        self.cell_width = int(self.winfo_width() / self.width_cells)
        self.height_cells = height_cells
        self.cell_height = int(self.winfo_height() / self.height_cells)

    def on_click(self, event):
        x_cell = int(event.x / self.cell_width)
        y_cell = int(event.y / self.cell_height)

        self.event_listener.click(x_cell, y_cell)

    def draw_game_state(self, game):
        self.delete("all")

        for row in game.height:
            y = row * self.cell_height
            for column in game.width:
                x = column * self.cell_height
                number = game.get(x, y)
                if number != 0:
                    self.create_rectangle(x, y, x + self.cell_width, self.cell_height, fill='red')
                    self.create_text(x + int(self.cell_width), y + int(self.cell_height), text=str(), fill='white')

    
