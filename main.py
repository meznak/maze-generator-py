# PyGame template.
 
# Import standard modules.
import sys
 
# Import non-standard modules.
import pygame as pg
from pygame.locals import *

# Import local modules
from maze import Maze

def update(dt, maze):
  """
  Update game. Called once per frame.
  dt is the amount of time passed since last frame.
  If you want to have constant apparent movement no matter your framerate,
  what you can do is something like
  
  x += v * dt
  
  and this will scale your velocity based on time. Extend as necessary."""
  
  # Go through events that are passed to the script by the window.
  for event in pg.event.get():
    # We need to handle these events. Initially the only one you'll want to care
    # about is the QUIT event, because if you don't handle it, your game will crash
    # whenever someone tries to exit.
    if event.type == QUIT:
      pg.quit() # Opposite of pg.init
      sys.exit(0) # Not including this line crashes the script on Windows. Possibly
      # on other operating systems too, but I don't know for sure.
    # Handle other events as you wish.
    if event.type == KEYDOWN and event.key == ord(' '):
      maze.reset()

  maze.update()
 
def draw(screen, maze: Maze):
  """
  Draw things to the window. Called once per frame.
  """
  # screen.fill(pg.Color('black')) # Fill the screen with black.
  
  # Redraw screen here
  changed_cells = maze.show(screen)
  
  # Flip the display so that the things we drew actually show up.
  pg.display.update(changed_cells)
 
def runpg(size = (100, 100), animate = True, profiling = False):
  # Initialise pg.
  pg.init()
  
  # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
  fps = 60.0
  fpsClock = pg.time.Clock()
  
  # Set up the window.
  width, height = 600, 600
  flags = DOUBLEBUF
  screen = pg.display.set_mode((width, height), flags)
  screen.set_alpha(None)
  pg.display.set_caption("Mazing")
  
  # screen is the surface representing the window.
  # pg surfaces can be thought of as screen sections that you can draw onto.
  # You can also draw surfaces onto other surfaces, rotate surfaces, and transform surfaces.
  
  # Set up the maze
  width = size[0]
  height = size[1]
  maze = Maze((width, height))

  # Main game loop.
  dt = 1/fps # dt is the time since last frame.
  # for i in range(7):
  while True: # Loop forever!
    update(dt, maze) # You can update/draw here, I've just moved the code for neatness.
    if animate or maze.finished:
      draw(screen, maze)
      dt = fpsClock.tick(fps)
      
      if maze.finished and profiling:
        pg.quit()
        sys.exit(0)

if __name__ == "__main__":
    runpg(size=(100,100))