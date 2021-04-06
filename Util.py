from Constants import *

def pm2pg(c):
  """pymunk and pygame disagree over where (0,0) is and what direction the y
  axis goes."""
  x,y = c
  return (int(x), int(HEIGHT-y))
