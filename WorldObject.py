import logging
import pymunk

class WorldObject:
  """Base class for objects that can exist in our world"""

  def __init__(self):
    pass

  def draw(self, display):
    pass

  def addToSpace(self, space):
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

  @property
  def position(self):
    return self.body.position

  @position.setter
  def position(self, p):
    self.body.position = p
