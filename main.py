import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
import pymunk
import random

from Constants import *
from Fish import Fish

pygame.init()

display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

space = pymunk.Space()
space.damping = SPEED_DAMPING

def mainloop():

  fish = Fish((50, 50))
  fish._body.body_type=pymunk.Body.KINEMATIC
  fish2 = Fish((200, 200))

  fish.addToSpace(space)
  fish2.addToSpace(space)

  walls = pymunk.Body(body_type=pymunk.Body.STATIC)
  space.add(walls)
  s = pymunk.Segment(walls, (0, 0), (WIDTH, 0), 1)
  s.elasticity = 1
  space.add(s)
  s = pymunk.Segment(walls, (WIDTH, 0), (WIDTH, HEIGHT), 1)
  s.elasticity = 1
  space.add(s)
  s = pymunk.Segment(walls, (WIDTH, HEIGHT), (0, HEIGHT), 1)
  s.elasticity = 1
  space.add(s)
  s = pymunk.Segment(walls, (0, 0), (0, HEIGHT), 1)
  s.elasticity = 1
  space.add(s)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    keys = pygame.key.get_pressed()

    vx, vy = 0, 0
    if keys[pygame.K_LEFT]:
      vx = -500
    elif keys[pygame.K_RIGHT]:
      vx = 500
    else:
      vx = 0

    if keys[pygame.K_UP]:
      vy = 500
    elif keys[pygame.K_DOWN]:
      vy = -500
    else:
      vy = 0

    fish._body.velocity = (vx, vy)

    if keys[pygame.K_j]:
      fish.body.angle += 1/180. * 3
    elif keys[pygame.K_k]:
      fish.body.angle -= 1/180. * 3

    display.fill((0, 0, 0))

    fish.draw(display)
    fish2.draw(display)

    pygame.display.update()
    clock.tick(FPS)
    space.step(1.0/FPS)

if __name__ == '__main__':
  mainloop()
  pygame.quit()

