from turtle import Turtle, Screen
import time
import drawers
import constants

sneggy = Turtle()
sneggy.shape("turtle")
screen = Screen()
screen.listen()
screen.setup(width=constants.WIDTH, height=constants.HEIGHT)


def turn(x_pos, y_pos):
    sneggy.setheading(x_pos + y_pos)


main_drawer = drawers.Drawer()
# main_drawer.draw_field()


screen.onclick(fun=sneggy.goto, btn=1)
screen.onclick(fun=turn, btn=3)


screen.mainloop()
