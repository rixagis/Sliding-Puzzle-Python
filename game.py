"""
Game model class
"""

import random

UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4

class Game:
    """Logical game board"""

    def __init__(self, width, height):
        """Create a board

        :param width: Width of the board in squares.
        :type width: int
        :param height: Height of the board in squares.
        :type height: int
        """
        self.width = width
        self.height = height
        self._empty_x = -1      #x-positon of empty cell
        self._empty_y = -1      #y-position of empty cell

        self.init_board()

    def init_board(self):
        """Fill the board with pieces and places them in initial positions"""
        self._board = []
        for x in range(self.width - 1):     #filling with columns and then with rows
            self._board.append([])           #to keep [x][y] addressing
            for y in range(self.height):
                self._board[x].append(y * self.width + x + 1)

        for y in range(self.height - 1):    #the last cell must be empty
            self._board[self.width-1].append(y * self.width + x + 1)

        self._board[self.width - 1].append(0)   #0 is the empty cell
        self._empty_x = self.width - 1  #should remember the position of the empty cell
        self._empty_y = self.height - 1 #to facilitate move method

    def get(self, x, y):
        """Get the value of the piece at (x, y) position.

        :param x: x-coord in squares
        :type x: int
        :param y: y-coord in squares
        :type y: int
        :return: The value of the piece at (x, y)
        :rtype: int
        """
        return self._board[x][y]

    def move(self, direction):
        """Moves the piece near the empty cell to the given direction.
        The direction determines the moving piece uniquely due to the rules of the game.
        If there is no legal move in given direction, nothing happens.

        :param direction: The direction in which the available piece should move.
        Named constants UP, RIGHT, DOWN and LEFT should be used.
        :type direction: int
        """
        x0, y0 = self._empty_x, self._empty_y
        if direction == UP:
            if y0 > 0:
                self._board[x0][y0] = self._board[x0][y0 - 1]
                self._board[x0][y0 - 1] = 0
                self._empty_y = y0 - 1
        elif direction == DOWN:
            if y0 < self.height - 1:
                self._board[x0][y0] = self._board[x0][y0 + 1]
                self._board[x0][y0 + 1] = 0
                self._empty_y = y0 + 1
        elif direction == LEFT:
            if x0 > 0:
                self._board[x0][y0] = self._board[x0 - 1][y0]
                self._board[x0 - 1][y0] = 0
                self._empty_x = x0 - 1
        elif direction == RIGHT:
            if x0 < self.width - 1:
                self._board[x0][y0] = self._board[x0 + 1][y0]
                self._board[x0 + 1][y0] = 0
                self._empty_x = x0 + 1

    def press(self, x, y):
        """Process player's press action:
        if the player presses a piece near the empty cell, that piece should move there.

            :param x: x-coord of the pressed cell
            :type x: int
            :param y: y-coord of the pressed cell
            :type y: int
        """
        if x < self.width - 1 and self._board[x+1][y] == 0:
            self.move(RIGHT)
        elif x > 0 and self._board[x-1][y] == 0:
            self.move(LEFT)
        elif y < self.height - 1 and self._board[x][y+1] == 0:
            self.move(DOWN)
        elif y > 0 and self._board[x][y-1] == 0:
            self.move(UP)

    def is_solved(self):
        """Check if the game is solved (if all the pieces are in initial positions).

        :return: `True` if the game is solved, `False` otherwise.
        :rtype: bool
        """
        solved = True
        for x in range(self.width - 1):
            for y in range(self.height):
                if self._board[x][y] != y * self.width + x + 1:
                    solved = False
        for y in range(self.height - 1):
            if self._board[self.width-1][y] != y * self.width + x + 1:
                solved = False
        if self._board[self.width-1][self.height-1] != 0:
            solved = False

        return solved

    def shuffle(self):
        """Shuffle the game board randomly.
        """
        move_count = random.randint(500, 1000)
        choices = [UP, DOWN, RIGHT, LEFT]
        direction = random.choice(choices)
        self.move(direction)
        for i in range(move_count):
            new_choices = choices[:]
            new_choices.remove(direction)   #remove the previously used direction
            direction = random.choice(new_choices)
            self.move(direction)
