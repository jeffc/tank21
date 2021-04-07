import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
import pymunk
import random

from Constants import *
from Fish import Fish
from Controller import KeyboardController

pygame.init()

display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

space = pymunk.Space()
space.damping = SPEED_DAMPING

def mainloop():

  fish = Fish((50, 50), space)
  #fish._body.body_type=pymunk.Body.KINEMATIC
  fish._controller = KeyboardController()
  fish2 = Fish((200, 200), space)

  fish.addToSpace(space)
  fish2.addToSpace(space)

  walls = pymunk.Body(body_type=pymunk.Body.STATIC)
  space.add(walls)
  s = pymunk.Segment(walls, (0, 0), (WIDTH, 0), 5)
  s.elasticity = 1
  space.add(s)
  s = pymunk.Segment(walls, (WIDTH, 0), (WIDTH, HEIGHT), 5)
  s.elasticity = 1
  space.add(s)
  s = pymunk.Segment(walls, (WIDTH, HEIGHT), (0, HEIGHT), 5)
  s.elasticity = 1
  space.add(s)
  s = pymunk.Segment(walls, (0, 0), (0, HEIGHT), 5)
  s.elasticity = 1
  space.add(s)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    display.fill((0, 0, 0))

    fish.draw(display)
    fish2.draw(display)

    pygame.display.update()
    clock.tick(FPS)
    
    fish.step(1.0/FPS)
    fish2.step(1.0/FPS)
    space.step(1.0/FPS)

if __name__ == '__main__':
  mainloop()
  pygame.quit()

