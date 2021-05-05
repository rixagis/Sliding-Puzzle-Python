from board_panel import BoardPanel

class BoardPanelImage(BoardPanel):

    def __init__(self, root, width_cells, height_cells, square_imgs, **kwargs):
        BoardPanel.__init__(self, root, width_cells, height_cells, **kwargs)
        self.square_imgs = square_imgs
    
    def draw_game_state(self, game):
        """Displays the state of the game in canvas.

        Args:
            game (Game): Game object which state should be diplayed.
        """
        self.delete("all")

        for row in range(game.height):
            y = row * self.cell_height
            for column in range(game.width):
                x = column * self.cell_width
                number = game.get(column, row)
                if number != 0:
                    self.create_image(int(x + self.cell_width/2), int(y + self.cell_height/2), image=self.square_imgs[number])