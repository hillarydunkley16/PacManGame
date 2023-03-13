Files required: main.py, classes.py, functions.py, graphics.py, ghost_lightblue.gif.



How to play: To run this game, click on the window after clicking run. The pacman and ghost will both begin to move. Then use arrow keys to control the pacman, keeping it away from the ghost and eating the pellets. You lose if the ghost catches up with you, and you win if you eat all the pellets.



A high-level description of the structure of the code:

Classes include a pacman class, ghost class, and a tile class. The pacman and ghost classes create a pacman or ghost which can be drawn and moved and return its center location and the coordinates of the tile it is in. The difference is that the pacman is a graphics.py circle while the ghost is an imported gif image. The tile class can be drawn, have its food status set (whether a pellet is present), and return its food status and its form (whether it is a wall, blank, etc.).

There is an animation loop, in which the pacman moves and eats pellets to increase the score, and the ghost moves and checks if it eats the pacman. The animation loop is initially triggered by the user clicking on the window: after the click, the direction of the pacman is controlled by the arrow keys.