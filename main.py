from graphics import *
from classes import *
from functions import *
from math import sqrt

def main():
  ''' Pacman game. Creates board, draws ghost and pacman, creates point counter, moves pacman and ghost in an animation loop, and ends when all pellets are eaten or ghost reaches pacman.
  '''
  win = GraphWin('getKey', 315, 405)
  win.setBackground('black')
  win.setCoords(0, 0, 28, 36)

  # Define initial board
  tiles = initial_board()
  # Draw board
  board(tiles, win)

  # Initial conditions of pac
  pac = Pacman(Point(14,9.5),win)
  pac.draw()
  aim = [-1,0]
  next_move = 'none'

  # Initial conditions of ghosts
  blue = Ghost(Point(14.5,21.5), win, 'ghost_lightblue.gif')
  blue.draw()
  blue_ghost_aim = [-1,0]

  # Initial conditions of point counter
  points = 0
  score = Text(Point(6,35.25), str('Score:'))
  score.setTextColor('white')
  score.setSize(12)
  score.draw(win)
  point_counter = Text(Point(6,33.75), str(points))
  point_counter.setTextColor('white')
  point_counter.setSize(12)
  point_counter.draw(win)

  # Don't start game until clicked
  win.getMouse()

  while True:
    # Pac movement
    x = win.checkKey()
    if x == 'Right':
      next_move = [1,0]
    if x == 'Left':
      next_move = [-1,0]
    if x == 'Up':
      next_move = [0,1]
    if x == 'Down':
      next_move = [0,-1]
    if x == 'q':
      break
    # Eat pellets
    pac_tileX = pac.getTileX()
    pac_tileY = pac.getTileY()
    if tiles[str(pac_tileX) + '_' + str(pac_tileY)].getFood() == 'pellet':
      points += 1
      point_counter.setText(points)
      tiles[str(pac_tileX) + '_' + str(pac_tileY)].setFood('none')
    if points == 246:
      end_text_1 = Text(Point(14,20), 'You win!')
      end_text_2 = Text(Point(14,16), 'Final score:' + str(points))
      end_text_1.setTextColor('green yellow')
      end_text_1.setSize(26)
      end_text_1.draw(win)
      end_text_2.setTextColor('green yellow')
      end_text_2.setSize(26)
      end_text_2.draw(win)
      break
      
    # Check if next move is allowed.
    if ((round(pac.getCenter().getX(),2) == pac_tileX + .5) and (round(pac.getCenter().getY(),2) == pac_tileY + .5)) or (aim == 'none'):
      next_key = 'a'
      if next_move in [[1,0],[-1,0],[0,1],[0,-1]]:
        next_key = str(pac_tileX + next_move[0]) + '_' + str(pac_tileY + next_move[1])
        aim = next_move
        if tiles[next_key].getForm() == 'wall':
          aim = 'none'
      if next_move == 'none' and aim != 'none':
        next_key = str(pac_tileX + aim[0]) + '_' + str(pac_tileY + aim[1])
        if tiles[next_key].getForm() == 'wall':
          aim = 'none'

    # Move pac.
    if aim in [[1,0],[-1,0],[0,1],[0,-1]]:
      pac.move(.01*aim[0],.01*aim[1])

    # Ghost movement
    # Only change direction when in center of a tile.
    if ((round(blue.getCenter().getX(),2) == blue.getTileX() + .5) and (round(blue.getCenter().getY(),2) == blue.getTileY() + .5)):
      blue_ghost_aim = getChaseAim(blue.getCenter(),pac.getCenter(),tiles,blue_ghost_aim)
    blue.move(.01*blue_ghost_aim[0],.01*blue_ghost_aim[1])
    # Check if ghost eats pac
    blue_front_point = Point(blue.getCenter().getX() + .5*blue_ghost_aim[0], blue.getCenter().getY() + .5*blue_ghost_aim[1])
    if sqrt((blue_front_point.getX()-pac.getCenter().getX())**2 + (blue_front_point.getY()-pac.getCenter().getY())**2) <= .5:
      end_text_1 = Text(Point(14,20), 'You lost!')
      end_text_2 = Text(Point(14,16), 'Final score:' + str(points))
      end_text_1.setTextColor('green yellow')
      end_text_1.setSize(26)
      end_text_1.draw(win)
      end_text_2.setTextColor('green yellow')
      end_text_2.setSize(26)
      end_text_2.draw(win)
      break
    

  win.getKey()
  win.close()

main()