# TODO: design the field
# TODO: design the pool with figures
# TODO: design the figures (turtles)
# TODO: design the placement / displacement function
# TODO: design the correct/incorrect position
# TODO: design level change
# TODO: design level navigation


from turtle import Turtle, Screen
import time
import drawers
import constants
import figures

# SCREEN MANUPULATIONS
screen = Screen()
screen.tracer(0)

sneggy = Turtle()
sneggy.penup()
sneggy.shape("circle")
sneggy.turtlesize(constants.FIGURE_COMPONENT_SIZE)


# This function moves the turtle to the cell that is closes to the clicked point on screen
def mark_closest(x, y):
    minimum_distance = None
    closest_cell = None
    for row in constants.FIELD_CELLS_CENTERS:
        for cell_center in constants.FIELD_CELLS_CENTERS[row]:
            sneggy.goto(cell_center)
            if not minimum_distance:
                closest_cell = cell_center
                minimum_distance = sneggy.distance(x, y)
            elif minimum_distance and sneggy.distance(x, y) < minimum_distance:
                closest_cell = cell_center
                minimum_distance = sneggy.distance(x, y)
    blue_figure.body[0].goto(closest_cell)
    blue_figure.positioning_blue()


# MAIN CYCLE
main_drawer = drawers.Drawer()

main_drawer.draw_field_from_centers()
main_drawer.draw_frame()

blue_figure = figures.Figure(color="blue", length=4)


screen.onclick(fun=mark_closest, btn=1)
screen.onclick(fun=blue_figure.turn_blue, btn=3)

for rows in constants.FIELD_CELLS_CENTERS:
    for cell in constants.FIELD_CELLS_CENTERS[rows]:
        print(cell)
    print(" ")

while True:
    screen.update()
    time.sleep(0.1)

# screen.onclick(fun=turn, btn=3)

screen.mainloop()
