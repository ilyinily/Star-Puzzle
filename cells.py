from turtle import Turtle
import constants


class Cell():
    def __init__(self, x_pos, y_pos, row, position, radius=constants.RADIUS):
        self.x_top_left = x_pos
        self.y_top_left = y_pos
        self.radius = radius
        self.row = row
        self.position = position
