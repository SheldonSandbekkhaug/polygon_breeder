import sys
import random
from global_functions import *

MAX_DELTA_COLOR = 60


class Polygon(object):
  """ Class to represent a polygon """
  def __init__(self):
    self.vertices = []
    self.color = randomize_color()

  def create_random(self, n):
    """ Create a random polygon with n vertices. """
    self.vertices = []
    for i in xrange(0, n):
      x = random.randint(0, PICTURE_SIZE)
      y = random.randint(0, PICTURE_SIZE)
      self.vertices.append((x, y))

    self.color = randomize_color()

    return self

  def mutate(self):
    """ Add a vertex, remove a vertex, or change the location of a vertex.
    Alternatively, translate the entire polygon.
    Return a new polygon. """
    new_polygon = Polygon()

    MUTATION_RATE = 0.5
    max_point_delta = 20

    # Buffer changes so we iterate correctly
    to_add = []

    action = random.random()
    if (action < 0.1):
      # Translate the entire polygon
      offset_x = randomize_with_bounds(0, max_point_delta, 0, PICTURE_SIZE)
      offset_y = randomize_with_bounds(0, max_point_delta, 0, PICTURE_SIZE)

      for vertex in self.vertices:
        # Translate all vertices and check that they're in bounds
        new_x = vertex[0]
        if (is_in_bounds(vertex[0] + offset_x, 0, PICTURE_SIZE)):
          new_x = vertex[0] + offset_x

        new_y = vertex[1]
        if (is_in_bounds(vertex[0] + offset_x, 0, PICTURE_SIZE)):
          new_y = vertex[1] + offset_y
        new_polygon.vertices.append((new_x, new_y))

    # Mutate color
    action = random.random()
    if (action < 0.1):
      # Same as parent
      new_polygon.color = self.color
    else:
      # Add some randomness to the color
      new_red = randomize_with_bounds(self.color[0], MAX_DELTA_COLOR,
        0, 255)
      new_green = randomize_with_bounds(self.color[1], MAX_DELTA_COLOR,
        0, 255)
      new_blue = randomize_with_bounds(self.color[2], MAX_DELTA_COLOR,
        0, 255)
      new_polygon.color = (new_red, new_green, new_blue)

    for vertex in self.vertices:
      action = random.random()
      if (action < MUTATION_RATE):
        # Mutate a vertex
        new_x = randomize_with_bounds(vertex[0], max_point_delta,
          0, PICTURE_SIZE)
        new_y = randomize_with_bounds(vertex[1], max_point_delta,
          0, PICTURE_SIZE)
        new_polygon.vertices.append((new_x, new_y))
      elif (action < MUTATION_RATE + 0.1):
        # Add a vertex
        new_x = random.randint(0, PICTURE_SIZE)
        new_y = random.randint(0, PICTURE_SIZE)
        to_add.append((new_x, new_y))
      elif (action < MUTATION_RATE + 0.2):
        # Remove a vertex by not adding it to the new polygon
        pass
      else:
        # Stay the same
        new_polygon.vertices.append(vertex)

    # Add vertices here so that we don't iterate new vertices
    for v in to_add:
      new_polygon.vertices.append(v)

    # Try again if we end up with 2 or less vertices
    if (len(new_polygon.vertices) <= 2):
      new_polygon = self.mutate()

    return new_polygon

  def print_polygon(self):
    """ Print a text representation of this polygon. """
    for v in self.vertices:
      sys.stdout.write("(%i, %i) " % (v[0], v[1]))
    sys.stdout.write("\n")
