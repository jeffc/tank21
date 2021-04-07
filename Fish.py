import pymunk
import pygame
from WorldObject import WorldObject
from Controller import Controller
from Util import *

from math import *

FISH_RADIUS = 20

class Fish(WorldObject):

  def __init__(self, position=(0,0)):
    super().__init__()
    self._body = pymunk.Body()
    self.position = position
    self._shape = pymunk.Circle(self.body, FISH_RADIUS)
    self._shape.density = 1
    self._shape.elasticity = 0.9
    self._shape.friction = 0.2
    self._controller = Controller()

  def draw(self, display):
    pygame.draw.circle(display,
        (128, 128, 255),
        pm2pg(self.position),
        FISH_RADIUS
    )

    pygame.draw.line(
        display,
        (0, 0, 0),
        pm2pg(self.position),
        pm2pg((
          round(self.position.x + FISH_RADIUS * self.body.rotation_vector.x),
          round(self.position.y + FISH_RADIUS * self.body.rotation_vector.y))
          )
        )


  def step(self, dt):

    o = self._controller.step(dt)
    impulse = o['FORWARD'] * 5e5

    self.body.apply_force_at_local_point(
        (impulse, 0),
        (0, 0)
    )

    self.body.angle += o['ROTATE'] * 8/180.



  def addToSpace(self, space):
    space.add(self.body, self.shape)

  def removeFromSpace(self, space):
    space.remove(self.shape)
    space.remove(self.body)
