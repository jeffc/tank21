import logging
import pymunk
from pygame import Color

class WorldObject:
  """Base class for objects that can exist in our world"""

  def __init__(self):
    self.should_remove = False
    self._color = Color(0, 0, 0)

  def draw(self, display):
    pass

  def step(self, dt):
    pass

  def addToSpace(self, space):
    pass

  def removeFromSpace(self, space):
    pass
  
  @property
  def body(self):
    if not hasattr(self, '_body'):
      logging.warning("Warning: called for body without a _body")
      self._body = pymunk.Body()
    return self._body

  @property
  def shape(self):
    if not hasattr(self, '_shape'):
      logging.warning("Warning: called for shape without a _shape")
      return None
    return self._shape

  @shape.setter
  def shape(self, s):
    s.parent = self
    self._shape = s

  @property
  def position(self):
    return self.body.position

  @position.setter
  def position(self, p):
    self.body.position = p

  @property
  def color(self):
    return self._color

  @color.setter
  def color(self, c):
    self._color = c
