import pymunk
import pygame
from WorldObject import WorldObject
from Util import *

FISH_RADIUS = 20

class Fish(WorldObject):

  def __init__(self, position=(0,0)):
    super().__init__()
    self._body = pymunk.Body()
    self.position = position
    self._shape = pymunk.Circle(self.body, FISH_RADIUS)
    self._shape.density = 1
    self._shape.elasticity = 1

  def draw(self, display):
    pygame.draw.circle(display,
        (128, 128, 255),
        pm2pg(self.position),
        FISH_RADIUS
    )


  def addToSpace(self, space):
    space.add(self.body, self.shape)