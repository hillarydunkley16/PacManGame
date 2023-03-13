from classes import *
from math import sqrt

def board(tiles, window):
  ''' tiles is a dictionary with keys of the form number1_number2 (including every combination of 0<=number1<28 and 0<=number2<36) which correspond to strings. window is the window in which the board is drawn. Reassigns each key to a Tile object and then draws the tiles.
  '''
  for i in range(28):
    for j in range(36):
      key = str(i) + '_' + str(j)
      if (tiles[key] == 'wall') or (tiles[key] == 'door') or (j>32) or (j<2) or ((13<=j<=23) and (7<=i<=20)) or ((13<=j<=23) and ((i<6) or (i>21))):
        tiles[key] = Tile(i,j,window,tiles[key],'none')
      else:
        tiles[key] = Tile(i,j,window,tiles[key],'pellet')
      tiles[key].draw()

def initial_board():
  ''' Returns a dictionary with keys of the form number1_number2 (including every combination of 0<=number1<28 and 0<=number2<36) which correspond to strings 'blank' or 'wall' or 'door', where number1 is the x-coordinate and number2 is the y-coordinate of a tile of a pacman board and the string corresponds to the form of that tile.
  '''
  tiles = {}
  # Start with a blank board to make sure every tile exists
  for i in range(28):
    for j in range(36):
      key = str(i) + '_' + str(j)
      tiles[key] = 'blank'
  # Define walls
  walls = []
  for i in (list(range(2,14)) + list(range(23,33))):
    walls.append('0' + '_' + str(i))
    walls.append('27' + '_' + str(i))
  for i in [2,7,8,13,23,32]:
    walls.append('1' + '_' + str(i))
    walls.append('26' + '_' + str(i))
  for i in [2,4,5,7,8,10,11,13,23,25,26,28,29,30,32]:
    walls.append('2' + '_' + str(i))
    walls.append('25' + '_' + str(i))
  for i in [2,4,5,10,11,13,23,25,26,28,29,30,32]:
    walls.append('3' + '_' + str(i))
    walls.append('24' + '_' + str(i))
  for i in [2,4,5,7,8,9,10,11,13,23,25,26,28,29,30,32]:
    walls.append('4' + '_' + str(i))
    walls.append('23' + '_' + str(i))
  for i in (list(range(13,24)) + [2,4,5,7,8,9,10,11,25,26,28,29,30,32]):
    walls.append('5' + '_' + str(i))
    walls.append('22' + '_' + str(i))
  for i in [2,4,5,32]:
    walls.append('6' + '_' + str(i))
    walls.append('21' + '_' + str(i))
  for i in (list(range(4,9)) + list(range(13,18)) + list(range(19,27)) + [2,10,11,28,29,30,32]):
    walls.append('7' + '_' + str(i))
    walls.append('8' + '_' + str(i))
    walls.append('19' + '_' + str(i))
    walls.append('20' + '_' + str(i))
  for i in [2,4,5,10,11,22,23,28,29,30,32]:
    walls.append('9' + '_' + str(i))
    walls.append('18' + '_' + str(i))
  for i in [2,4,5,7,8,10,11,13,14,16,17,18,19,20,22,23,25,26,28,29,30,32]:
    walls.append('10' + '_' + str(i))
    walls.append('17' + '_' + str(i))
  for i in [2,4,5,7,8,10,11,13,14,16,20,22,23,25,26,28,29,30,32]:
    walls.append('11' + '_' + str(i))
    walls.append('16' + '_' + str(i))
  for i in [2,7,8,13,14,16,20,25,26,32]:
    walls.append('12' + '_' + str(i))
    walls.append('15' + '_' + str(i))
  for i in (list(range(4,9)) + list(range(10,15)) + list(range(22,27)) + list(range(28,33)) + [2,16]):
    walls.append('13' + '_' + str(i))
    walls.append('14' + '_' + str(i))
  for wall in walls:
    tiles[wall] = 'wall'
  tiles['13_20'] = 'door'
  tiles['14_20'] = 'door'
  return tiles

def getChaseAim(ghost_center, pac_center, tiles, current_aim):
  ''' ghost_center and pac_center are Point objects. tiles is a dictionary of keys of the form number1_number2 which correspond to Tile objects. current_aim is a list [x,y] which is a unit vector. Returns a list which is a unit vector in the direction that the ghost can move in which will move the ghost closest to the pacman.
  '''
  # Turn points into coordinates.
  ghost_x = ghost_center.getX()
  ghost_y = ghost_center.getY()
  pac_x = pac_center.getX()
  pac_y = pac_center.getY()

  # Get unit vector pointing from ghost towards pac.
  vec = [pac_x - ghost_x, pac_y - ghost_y]
  vec_len = sqrt(vec[0]**2+vec[1]**2)
  unit_vec = [vec[0]/vec_len, vec[1]/vec_len]

  # Get tile coordinates of ghost location.
  tile_x = int(ghost_x)
  tile_y = int(ghost_y)

  # Get directions the ghost can move in.
  options = []
  key_r = str(tile_x+1) + '_' + str(tile_y)
  key_l = str(tile_x-1) + '_' + str(tile_y)
  key_u = str(tile_x) + '_' + str(tile_y+1)
  key_d = str(tile_x) + '_' + str(tile_y-1)
  if tiles[key_r].getForm() == 'blank':
    options.append([1,0])
  if tiles[key_l].getForm() == 'blank':
    options.append([-1,0])
  if tiles[key_u].getForm() == 'blank':
    options.append([0,1])
  if tiles[key_d].getForm() == 'blank':
    options.append([0,-1])
  # Ghost cannot reverse direction.
  if [-1*current_aim[0],-1*current_aim[1]] in options:
    options.remove([-1*current_aim[0],-1*current_aim[1]])
  
  # Get most accurate possible direction.
  best = options[0]
  for option in options:
    if sqrt((unit_vec[0]-option[0])**2+(unit_vec[1]-option[1])**2) < sqrt(best[0]**2+best[1]**2):
      best = option

  # Return direction
  return best