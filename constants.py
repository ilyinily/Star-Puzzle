import math

# CONSTANTS FOR THE FIELD
WIDTH = 400
HEIGHT = 300
PADDING_X = 40
PADDING_Y = 20
SIZE = 36
RADIUS = math.floor(0.8660 * SIZE)  # This value is calculated as cosine of 60 degrees multiplied by SIZE
FIELD_TOP_X = RADIUS * -2
FIELD_TOP_Y = RADIUS * 7.2
VERTICES = ('top', 'upper right', 'lower right', 'bottom', 'lower left', 'upper left')
UPPER_LINE_LENGTH = 7
LOWER_LINE_LENGTH = 6
PENSIZE = 3
FIELD_CELLS_CENTERS = {'topmost_row': [],
                       'upper_row': [],
                       'lower_row': [],
                       'bottom_row': [], }


# Assigning values to FIELD_CELLS_CENTERS:
for cell in range(UPPER_LINE_LENGTH):
    FIELD_CELLS_CENTERS['topmost_row'].append((FIELD_TOP_X + RADIUS * cell * 2, round(FIELD_TOP_Y, 0)))

for cell in range(LOWER_LINE_LENGTH):
    FIELD_CELLS_CENTERS['upper_row'].append((FIELD_TOP_X + RADIUS + RADIUS * cell * 2, round(FIELD_TOP_Y - SIZE - RADIUS / 2 - 2, 0)))

for cell in range(UPPER_LINE_LENGTH):
    FIELD_CELLS_CENTERS['lower_row'].append((FIELD_TOP_X + RADIUS * cell * 2, round(FIELD_TOP_Y - SIZE * 3, 0)))

for cell in range(LOWER_LINE_LENGTH):
    FIELD_CELLS_CENTERS['bottom_row'].append((FIELD_TOP_X + RADIUS + RADIUS * cell * 2, round(FIELD_TOP_Y - SIZE - RADIUS * 4 - 2, 0)))

# CONSTANTS FOR FIGURES AND FIGURE COMPONENTS
FIGURE_COMPONENT_SHAPE = "circle"
FIGURE_COMPONENT_SIZE = 2.5
FIGURE_INITIAL_VERTICAL_OFFSET_RATIO = 1.974 # Counted manually to allow good placement to the field
FIGURE_SECONDARY_VERTICAL_OFFSET_RATIO = 1.742

