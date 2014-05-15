import random


from polygon import Polygon


class Picture(object):
  """ Class to represent a picture """
  def __init__(self):
    self.polygons = []

  def create_random(self, n):
    """ Create n polygons with random vertices. The dimensions of each
    picture should be specified with max_x and may_y.
    
    """
    self.polygons = []
    for i in xrange(0, n):
      p = Polygon()
      # 3 to 5 vertices
      Polygon.create_random(p, random.randint(3,5))
      self.polygons.append(p)
    return self

  def mutate(self):
    """ Create a new picture by mutating a polygon, adding a polygon,
    or removing a polygon.
    Return a new picture

    """
    new_picture = Picture()
    
    # Buffer changes so we iterate correctly
    to_add = []

    for polygon in self.polygons:
      mutation_type = random.random()
      if (mutation_type < 0.1):
        # Stay the same
        new_polygon = Polygon()
        new_polygon.vertices = list(polygon.vertices)
        to_add.append(new_polygon)
      if (mutation_type < 0.8):
        # Do some mutation
        to_add.append(polygon.mutate())
      elif (mutation_type >= 0.8 and mutation_type < 0.9):
        # Add a polygon
        new_polygon = Polygon()
        new_polygon = new_polygon.create_random(3)
        to_add.append(new_polygon)
      elif (mutation_type >= 0.9):
        # Remove a polygon by not adding it to the new picture
        if (len(self.polygons) <= 1):
          # Mutate instead if there is only one polygon left
          to_add.append(polygon.mutate())
        else:
          pass

    # Add polygons here so that we don't iterate over new polygons
    for p in to_add:
      new_picture.polygons.append(p)

    return new_picture

  def print_picture(self):
    """ Print a text representation of this picture. """
    for p in self.polygons:
      p.print_polygon()
