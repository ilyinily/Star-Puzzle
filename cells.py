from turtle import Turtle
import constants
import figures


class Cell:
    def __init__(self, x_pos, y_pos, row, position, radius=constants.RADIUS):
        self.x_center = x_pos
        self.y_center = y_pos
        self.radius = radius
        self.row = row
        self.position = position
        self.taken_by: figures.Figure