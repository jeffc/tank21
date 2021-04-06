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
#space.gravity = 0, -1000

BALL_RADIUS = 50

def coord(c):
  return c[0], HEIGHT-c[1]

def mainloop():

  ball = Fish((50, 50))
  ball._body.body_type=pymunk.Body.KINEMATIC
  ball2 = Fish((200, 200))

  ball.addToSpace(space)
  ball2.addToSpace(space)

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

    ball._body.velocity = (vx, vy)

    display.fill((0, 0, 0))

    ball.draw(display)
    ball2.draw(display)

    pygame.display.update()
    clock.tick(FPS)
    space.step(1.0/FPS)

if __name__ == '__main__':
  mainloop()
  pygame.quit()

