from turtle import Turtle
import constants


class BaseFigure(Turtle):
    def __init__(self, shape=constants.FIGURE_COMPONENT_SHAPE):
        super(BaseFigure, self).__init__()
        self.penup()
        self.head = False
        self.shape(shape)
        self.turtlesize(constants.FIGURE_COMPONENT_SIZE)


class Figure:
    def __init__(self, length=4, color="black"):
        self.body = []
        for component in range(length):
            self.body.append(BaseFigure())
            self.body[len(self.body) - 1].color(color)
        self.body[0].head = True

    def positioning_blue(self):
        self.body[1].setposition(self.body[0].position()[0] - constants.RADIUS * 2, self.body[0].position()[1])
        self.body[2].setposition(self.body[0].position()[0] + constants.RADIUS * 2, self.body[0].position()[1])
        self.body[3].setposition(self.body[0].position()[0] - constants.RADIUS * 1, self.body[0].position()[1] + constants.RADIUS * constants.FIGURE_SECONDARY_VERTICAL_OFFSET_RATIO)

    def turn_blue(self, x, y):
        self.body[1].circle(-constants.RADIUS * 2, 60)
