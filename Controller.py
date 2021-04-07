import pygame

class Controller:
  """Superclass for ways that a fish can be controlled."""

  OUTPUTS = [
      'FORWARD',
      'ROTATE',
  ]

  def __init__(self):
    pass

  def step(self, dt):
    return { o: 0.0 for o in self.OUTPUTS }


class KeyboardController(Controller):

  def step(self, dt):
    o = super().step(dt)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
      o['FORWARD'] = 1
    elif keys[pygame.K_DOWN]:
      o['FORWARD'] = -1

    if keys[pygame.K_LEFT]:
      o['ROTATE'] = 1
    elif keys[pygame.K_RIGHT]:
      o['ROTATE'] = -1

    return o
