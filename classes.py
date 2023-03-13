from graphics import *

class Pacman:
  def __init__(self,center,win):
    self.win = win
    self.center = center
    self.circ = Circle(self.center,.5)

  def draw(self):
    self.circ.draw(self.win)
    self.circ.setFill('yellow')

  def move(self,x,y):
    self.circ.move(x,y)

  def getTileX(self):
    x = self.circ.getCenter().getX()
    x = int(x)
    return x

  def getTileY(self):
    y = self.circ.getCenter().getY()
    y = int(y)
    return y

  def getCenter(self):
    return self.circ.getCenter()

class Tile:
  def __init__(self,lower_x,lower_y,win,form,food):
    self.win = win
    self.lower_x = lower_x
    self.lower_y = lower_y
    self.form = form
    self.food = food
    self.pellet = Circle(Point(self.lower_x+.5,self.lower_y+.5),.1)
    self.pellet.setFill('white')
    self.pellet.setOutline('white')
    
  def draw(self):
    rect = Rectangle(Point(self.lower_x,self.lower_y),Point(self.lower_x+1,self.lower_y+1))
    if self.form == 'blank':
      rect.setFill('black')
      rect.setOutline('black')
    if self.form == 'wall':
      rect.setFill('blue')
      rect.setOutline('blue')
    if self.form == 'door':
      rect.setFill('pink')
      rect.setOutline('pink')
    rect.draw(self.win)
    if self.food == 'pellet':
      self.pellet.draw(self.win)

  def getForm(self):
    return self.form

  def getFood(self):
    return self.food

  def setFood(self,new_food):
    self.food = new_food
    if self.food == 'none':
      self.pellet.undraw()
    if self.food == 'pellet':
      self.pellet.draw(self.win)

class Ghost:
  def __init__(self,center,win, file_name):
    self.win = win
    self.center = center
    #my attempt at inserting a ghost image:
    self.ghost_image = Image(self.center, file_name)

  def draw(self):
    self.ghost_image.draw(self.win)

  def move(self,x,y):
    self.ghost_image.move(x,y)
    self.center.move(x,y)

  def getTileX(self):
    x = self.center.getX()
    x = int(x)
    return x

  def getTileY(self):
    y = self.center.getY()
    y = int(y)
    return y

  def getCenter(self):
    return Point(self.center.getX(), self.center.getY())