#!/usr/bin/env python

""" polygon_breeder.py
Author: Sheldon Sandbekkhaug

"""

import sys
import math
import time
import pygame
import random
from pygame.locals import *


from global_functions import *
from picture import Picture
from polygon import Polygon


display = None

pictures = []

# Playing area boundaries
WEST_BOUND = 0
EAST_BOUND = GAME_WIDTH
NORTH_BOUND = 0
SOUTH_BOUND = GAME_HEIGHT


def play_game():
  """ Initialize and run the game loop. """
  global pictures
  pictures = init()

  #run game at 30 frames per second
  FPS = 30
  FPSCLOCK = pygame.time.Clock()

  playing = True

  # Main game loop
  while (playing == True):
    playing = handle_key_events()
    render(pictures)
    FPSCLOCK.tick(FPS)

  pygame.quit()
  sys.exit()


def init():
  """Initialize the game state. """
  pygame.init()

  global display
  display = pygame.display.set_mode((GAME_WIDTH,GAME_HEIGHT),0,32)

  pygame.display.set_caption('Polygon Breeder')

  return create_initial_pictures()


def create_initial_pictures():
  """ Create a randomized group of 9 pictures. """
  pictures = []

  for i in xrange(0, 9):
    pic = Picture()
    pic = Picture.create_random(pic, 1)

    pictures.append(pic)

  return pictures


def handle_key_events():
  """Respond to user keyboard input. """
  playing = True
  for event in pygame.event.get():
    # Allow the user to quit
    if event.type==QUIT:
      playing = False
    if event.type==KEYDOWN and event.key == K_ESCAPE:
      playing = False

    # If the user clicks on a picture, do some breeding
    if event.type==MOUSEBUTTONUP:
      mouse_pos = pygame.mouse.get_pos()
      picture_index = point_to_picture(mouse_pos)

      global pictures
      if (picture_index >= 0 and picture_index < len(pictures)):
        picture = pictures[picture_index]
        pictures = create_new_generation(picture, picture_index)

  return playing


def render(pictures):
  """ Draw graphics. Draw each picture in pictures. """
   # Display the background
  display.fill(BLACK)

  # Draw each picture
  i = 0 # Number of pictures drawn
  for picture in pictures:
    offsets = get_offsets(i)

    for polygon in picture.polygons:
      # Adjust vertices so pictures aren't overlapping
      adjusted_vertices = []

      for v in polygon.vertices:
        adjusted_vertices.append((v[0] + offsets[0], v[1] + offsets[1]))
      pygame.draw.polygon(display, polygon.color, adjusted_vertices)

    i += 1

  pygame.display.update()


def get_offsets(i):
  """ Get the x and y offsets for the i'th picture drawn this tick. """
  x = (i % 3) * (100 + PICTURE_BORDER) + PICTURE_BORDER
  if (i < 3):
    y = PICTURE_BORDER
  elif (i >= 3 and i <= 5):
    y = (100 * 1) + (2 * PICTURE_BORDER)
  else:
    y = (100 * 2) + (3 * PICTURE_BORDER)
  return (x, y)


def point_to_picture(point):
  """ Given a tuple containing the x-y position of a point, return the
  picture index of the picture at that location.

  """
  x = point[0]
  y = point[1]

  # Tells which picture column this point is in
  col = (x - PICTURE_BORDER) / (100 + PICTURE_BORDER)
  
  # Get which picture row the point is in
  row = 0
  if (y < (PICTURE_BORDER + 100)):
    row = 0
  elif (y < ((100 * 1) + (2 * PICTURE_BORDER) + 100)):
    row = 1
  else:
    row = 2 # There are only three rows

  return col + 3*row


def create_new_generation(picture, picture_index):
  """ Create nine new pictures mutated from picture. """
  new_pictures = []

  # Mutate each picture
  for i in xrange(0, 9):
    if (i != picture_index):
      p = Picture()
      p = picture.mutate()

      new_pictures.append(p)
    else:
      new_pictures.append(picture)

  return new_pictures


if (__name__=="__main__"):
  play_game()
