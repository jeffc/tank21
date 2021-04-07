import pymunk
import pygame
from WorldObject import WorldObject
from Controller import Controller
from Util import *

from math import *

FISH_RADIUS = 20
FISH_VIEW_DIST = 200
NUM_EYES = 5
VIEW_ANGLE = 30

class Fish(WorldObject):

  def __init__(self, position=(0,0), space=None):
    super().__init__()
    self._body = pymunk.Body()
    self.position = position
    self.shape = pymunk.Circle(self.body, FISH_RADIUS)
    self._shape.density = 1
    self._shape.elasticity = 0.9
    self._shape.friction = 0.2
    self._controller = Controller()
    self.color = pygame.Color(128, 128, 255)
    self._space = space

    # senses
    self._eyes = { 
        radians((a-((NUM_EYES-1)/2)) * (VIEW_ANGLE/NUM_EYES)):
          (pygame.Color(0,0,0), None)
        for a in range(NUM_EYES)
    }

  def draw(self, display):
    pygame.draw.circle(display,
        self.color,
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

    def eye(angle=0):
      eye_angle = self.body.rotation_vector.rotated(angle)
      segment_start = self.position + eye_angle * (FISH_RADIUS + 5)
      segment_end = segment_start + eye_angle * FISH_VIEW_DIST

      obj = self._space.segment_query_first(
          segment_start, segment_end, 4, pymunk.ShapeFilter(categories=pymunk.ShapeFilter.ALL_CATEGORIES())
      )

      if obj is not None and hasattr(obj.shape, 'parent'):
        pygame.draw.line(
            display,
            obj.shape.parent.color,
            pm2pg(segment_start),
            pm2pg(segment_start + eye_angle*obj.alpha*FISH_VIEW_DIST), 
            2
        )

    _ = [eye(a) for a in self._eyes.keys() ]

  def step(self, dt):
    o = self._controller.step(dt)
    impulse = o['FORWARD'] * 5e5

    self.body.apply_force_at_local_point(
        (impulse, 0),
        (0, 0)
    )

    self.body.angle += o['ROTATE'] * 15/180.

  def addToSpace(self, space):
    space.add(self.body, self.shape)

  def removeFromSpace(self, space):
    space.remove(self.shape)
    space.remove(self.body)
