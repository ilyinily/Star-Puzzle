import math

WIDTH = 1200
HEIGHT = 600
FIELD_TOP_X = -200
FIELD_TOP_Y = 100
SIZE = 40
RADIUS = math.floor(0.8660 * SIZE)  # This value is calculated as cosine of 60 degrees multiplied by SIZE
VERTICES = ('top', 'upper right', 'lower right', 'bottom', 'lower left', 'upper left')