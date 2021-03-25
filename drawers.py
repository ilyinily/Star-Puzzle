from turtle import Turtle
import constants


class Drawer(Turtle):
    def __init__(self):
        super(Drawer, self).__init__()
        self.coordinates = {}
        self.speed("fastest")
        self.penup()
        self.setposition(constants.FIELD_TOP_X, constants.FIELD_TOP_Y)
        self.hideturtle()

    def draw_hexagon(self, size=constants.SIZE):
        self.pendown()
        self.setheading(90)
        for i in range(10):
            self.forward(size)
            self.right(60)
        self.right(120)

    def draw_hexagon_center(self, x_center, y_center, size=constants.SIZE):
        self.penup()
        self.setposition(x=x_center, y=y_center)
        self.setheading(90)
        for i in range(6):
            self.forward(size)
            self.coordinates[constants.VERTICES[i]] = self.position()
            self.backward(size)
            self.right(60)
        for i in range(len(self.coordinates)):
            self.setposition(self.coordinates[constants.VERTICES[i]])
            self.pendown()
        self.setposition(self.coordinates[constants.VERTICES[0]])
        self.penup()
        self.setposition(x=x_center, y=y_center)

    def draw_line_of_hexagons(self, line_length=8, size=constants.SIZE):
        for i in range(line_length):
            self.draw_hexagon(size)
        self.left(120)
        self.penup()
        for i in range(line_length - 1):
            self.forward(size)
            self.right(60)
            self.forward(size)
            self.left(60)
        self.forward(size)
        self.left(60)
        self.forward(size)
        self.setheading(90)

    def draw_field(self, size=constants.SIZE):
        self.draw_line_of_hexagons(line_length=7, size=constants.SIZE)
        self.draw_line_of_hexagons(line_length=6, size=constants.SIZE)
        for i in range(3):
            self.forward(size)
            self.left(60)
        self.forward(size)
        self.setheading(90)
        self.draw_line_of_hexagons(line_length=7, size=constants.SIZE)
        self.draw_line_of_hexagons(line_length=6, size=constants.SIZE)
