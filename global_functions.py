""" File containing commonly-used constants and functions. """

import random



PICTURE_SIZE = 100

PICTURE_BORDER = 40

GAME_WIDTH = PICTURE_BORDER + (PICTURE_SIZE * 3) + (PICTURE_BORDER * 3)
GAME_HEIGHT = GAME_WIDTH

# Directions
EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
DARK_BROWN = (51,51,0)
YELLOW = (255,2550)


def randomize_with_bounds(old, delta, min, max):
  """ Randomize an integer between -delta and delta. Add that integer
  to old. If the new value is between min and max, return it.
  Otherwise, return min or max, whichever is closer to the new value.

  """
  new_value = old + random.randint(-delta, delta)
  if (new_value < min):
    return min
  elif (new_value > max):
    return max
  return new_value

def is_in_bounds(value, min, max):
  """ Return True if min <= value >= max
  Return False otherwise

  """
  if (min <= value and value <= max):
    return True
  return False

def randomize_color():
  """ Return a tuple with three integers between 0 and 255 inclusive. """
  red = random.randint(0, 255)
  green = random.randint(0, 255)
  blue = random.randint(0, 255)
  return (red, green, blue)
