# -*- coding: utf-8 -*-
"""
This is an implementation of the game Sokoban using object-oriented Python 
with pyprocessing providing the visuals.

Much of the code is provided for you. Scattered throughout the code 
are portions that you need to implement. Your first task will 
be to read through all of the code and understand what it is doing. 
Once you have done that, you should start adding in the missing
pieces to turn this into a working game. The missing pieces will be 
marked with comments, and in most cases a `pass`. This is just a filler 
command for empty blocks. Make sure to remove it when you add your own code.

More details are in the assignment write up.

@author: Gray Goolsby
Lab: X
Date: 5-5-17
"""


from pyprocessing import *




# Some constants that control the size of the window and the size of the tiles on the board
WIDTH = 600
HEIGHT = 600
CELL_SIZE= 25

class Tile:
    """
    This class implements a single tile on our game board.
    
    The tile is the basic unit of the game board. A tile can be open 
    or a wall. Open tiles are allowed to have an occupant (a game piece 
    positioned on it -- note that there can be at most one occupant).
    The tile is responsible for managing the piece placed upon it, reporting 
    when the square is open on the board, and passing drawing commands 
    along to any piece currently occupying it.
    """
    
    def __init__(self, tileType, x, y, gameBoard):
        """
        Initialize the tile, setting its position and default values.
        """
        self.tileType = tileType
        self.x = x
        self.y = y
        self.gameBoard = gameBoard
        self.goal = False
        self.occupant = None
        
    def draw(self):
        """
        Draw the tile and tell any occupant to draw itself.
        
        The drawing code is configured such that the current origin 
        of the coordinate system is in the middle of where the tile 
        should be drawn. As a result, the tile (and the pieces) 
        should draw themselves centered on (0,0).
        """

        
        if self.tileType=='o':
            rectMode(CENTER)
            fill(255,255,255)
            rect(0,0,CELL_SIZE, CELL_SIZE)
        if self.tileType=='w':
            rectMode(CENTER)
            fill(0,0,255)
            rect(0,0,CELL_SIZE,CELL_SIZE)
        if self.goal== True:
            rectMode(CENTER)
            fill(255,255,255)
            rect(0,0,CELL_SIZE,CELL_SIZE)
            fill(255,50,50)
            ellipse(0,0, CELL_SIZE-15, CELL_SIZE-15)
        
        
        # DON'T REPLACE THIS PART; LEAVE IT HERE
        # check if there is a piece here and tell it to draw itself if there is
        if self.occupant:
            self.occupant.draw()
            
    def isFree(self):
        """
        Return True if a piece could be moved on to this tile. 
        Return False if this is a wall, or there is already a piece here.
        """
        return self.tileType != 'w' and self.occupant == None
            
        
    def removePiece(self):
        """
        Remove the occupant from the tile. This sets the tile's occupant 
        property to None and also removes the occupant's reference to the 
        tile at the same time.
        """
        piece = self.occupant
        self.occupant = None
        if piece is not None:
            piece.tile = None
        return piece

    def addPiece(self, piece):
        """
        This adds a piece to the tile.
        
        It updates the tile's occupant property and gives the piece 
        a reference to itself.
        """
        self.occupant = piece
        piece.tile = self

    def getNeighbor(self, direction):
        """
        This gets the immediate neighbor of the tile in one of the 
        four cardinal directions: 'N', 'S', 'E', or 'W'. 
        
        To do this, it calculates the new x,y location of the 
        neighboring tile based on this tile's x,y position, and 
        then asks the game board which tile that location corresponds to
        using the getTile() method.
        
        """
        newx = self.x
        newy = self.y
        if direction == 'N':
            newy -= 1
        elif direction == 'S':
            newy += 1
        elif direction == 'W':
            newx -= 1
        elif direction == 'E':
            newx += 1
        return self.gameBoard.getTile(newx,newy)
            
        
           
class Box():
    """
    This class describes the Box objects.
    
    Boxes do not have much to do. They are moved around by the 
    other objects on the board. The only property that they have 
    is the tile that they are currently on.
    
    The only method they provide is draw(), which provides 
    the visual representation.
    """
    
    def __init__(self):
        """
        Initialize the Box and make it valid.
        
        We start by setting the tile to None (i.e., nothing). 
        When we put the piece on the board, this will be updated.
        """
        self.tile = None
    
    def draw(self):
        """
        Draw the visual representation of the Box.
        
        This can be anything, but it would be good if it was not 
        dramatically larger than CELL_SIZE. Also note that you should draw 
        as if the origin of the coordinate system (0,0) is in the center 
        of the tile this piece is currently on (i.e., draw your shape 
        centered on (0,0)).
        """
        rectMode(CENTER)
        fill(255,0,0)
        rect(0,0,CELL_SIZE,CELL_SIZE)
        

        
class Player():
    """
    This class describes the Player class.
    
    The Player object has a little more functionality than the other pieces.
    In addition to the tile the player is currently on, the player also 
    maintains a reference to the main game board so that it can interact 
    with the game.
    
    """
    def __init__(self, gameBoard):
        """
        Initialize the player.
        """
        self.gameBoard = gameBoard
        self.tile = None
        
        
    def draw(self):
        """
        Draw the visual representation of the Player.
        
        Like the Box, this can be anything. Just make sure it fits within 
        the CELL_SIZE and that it is centered on (0,0).
        """
        rectMode(CENTER)
        fill(255, 102, 204)
        ellipse(0,0,CELL_SIZE-5,CELL_SIZE-5)
        
        
    def move(self, direction):
        """
        This function is called in response to a key press event. 
        
        - Find the tile that you want to move to (the player's tile's neighbor)
        - check if the tile already has an occupant
        -- if yes, tell the game board to try to move it in the direction 
           the player is traveling
        -- if there are no obstructions on the far side, the piece will move; 
           if there are, it will not
        - tell the game board to try and move the player in the appropriate direction 
        """
        
        tile = self.tile #this gives the players location
        neighbor = tile.getNeighbor(direction)
        if neighbor.isFree() == False and neighbor.occupant != None: #checks if its a box
            nextNeighbor = neighbor.getNeighbor(direction)  
            if nextNeighbor.isFree():
                game.movePiece(neighbor.occupant, direction) #moves box
        game.movePiece(self,direction) #moves player
        

class SokobanBoard:
    """
    This class represents our game.
    
    The class is responsible for reading in the data files, 
    holding the game board and managing game play.
    
    The class has four pieces of data that it maintains:
    
    grid - a 2D list of Tile objects that represents the game board; 
    The tiles are arranged in the list just as they should be drawn
    
    boxes - a list of all of the Box objects currently on the board
    
    player - a Player object
    
    level - the current level number
    
    You are welcome to add more as needed.
    
    """
    
    
    # Constants - these are used to help read the data files
    # most are providing the interpretation of the characters you will find in the files
    OPEN = ' '
    WALL = '#'
    PLAYER = '@'
    BOX = '$'
    GOAL = '.'       # should have a box on it by the end
    BOXGOAL = '*'    # a goal that already has a box on it
    MAX_LEVEL = 90
    
    
    def __init__(self):
        """
        Initialize the game board.
        
        All this needs to do is set the first level and call 
        loadLevel() to read in the file for the level.
        """
        
        self.level = 0   
        self.loadLevel()
        self.counter= 0
        
        

    def loadLevel(self):
        """
        This function loads the current level, reading the description 
        from the appropriate input file.
        
        Don't worry too much about the implementation of this function (though 
        reading through it and understanding it would be a very good exercise).
        If this works, the grid will be set properly, and the pieces positioned on 
        the board in the correct positions.
        
        If you have anything that needs to be initialized or changed at the start
        of each level, this would be the place to do it -- probably up at the top 
        where the grid and boxes are re-initialized.
        """

        # reinitialize the collection of tiles and the obstacles
        self.grid = []
        self.boxes = []
      
        # read the data in from the correct file
        fname = os.path.join('levels', 'level.%02d.txt' % self.level)
       
        try:
           f = open(fname)
           data = []
           self.cols = 0
           for line in f:
               line = line.rstrip('\n')
               if len(line) > self.cols:
                   self.cols = len(line)
               data.append(line)
               
           f.close()
           self.rows = len(data)

           # Use the textual data to construct the maze and place the objects.
           # At the end we should have a 2D list of tiles and all of the pieces
           # in place on the board. 
           for y in range(self.rows):
             
               row = []
               for x in range(self.cols):
                    if x < len(data[y]):
                       squareType = data[y][x]
                    else:
                       squareType = self.OPEN
                    
                    if squareType == self.WALL:
                        # tile is a wall
                        tile = Tile('w', x,y, self)
                    else:
                        # tile is open, but might have something there
                        tile = Tile('o', x,y, self)
                     
                        if squareType == self.PLAYER:
                            # tile has the player on it
                            self.player = Player(self)
                            tile.addPiece(self.player)
                            
                        if squareType == self.GOAL or squareType == self.BOXGOAL:
                            # tile is a goal
                            tile.goal = True
                            
                        if squareType == self.BOX or squareType == self.BOXGOAL:
                            # tile has a Box on it
                            box = Box()
                            tile.addPiece(box)
                            self.boxes.append(box)

                    row.append(tile)    
               self.grid.append(row)   
        

        except IOError:
            # Some error handling if the file containing the maze can't be found.
            # If you see these messages, you probably have misplaced the levels folder.
            print("Error: cannot open " + fname)
            print("You need to have the 'levels' folder in this folder")
            print("Current folder is:")
            print(os.getcwd())
            sys.exit(1) 
    
    def getTile(self, x, y):
        """
        This is a convenience function to make it easier to access a 
        particular tile in the grid.
        """
        return self.grid[y][x]
        
    def movePiece(self, piece, direction):
        """
        Move a piece (either the player or a box) one step in one of the four 
        cardinal directions: 'N','E','S', or 'W' if it is possible. 
        
        - Find the tile the piece should be moved to (the piece's tile's neighbor)
        - Check if the tile is free
        -- if it is, remove the pieec from its current tile
        -- and add it to the new tile
        
        Note that if the destination is not free, you should do nothing -- the 
        piece will remain where it is.
        
        
        """
        
        tile = piece.tile
        neighbor = tile.getNeighbor(direction) 
        if neighbor.isFree():
            tile.removePiece()
            neighbor.addPiece(piece)
            
        


            
    def levelComplete(self):
        """
        This function should return True if the level is complete, and False if it is not.
        The level is complete when every box is on a goal tile.
        """
        
             
        for b in self.boxes:
            if b.tile.goal == False:
                return False
        return True
            
        
    
            
            
    def draw(self):
        """
        This is the master draw function that is called by pyprocessing's event handler.
        
        This sets the background color, centers the board and then draws each tile. The 
        translate() function moves the origin of the coordinate system. The first call is 
        setting the origin to the upper left hand corner of the board. The calls in the for 
        loops are making sure that the origin is in the center of where the tile should be 
        drawn so that all of the tiles and pieces can be drawn centered on the origin.
        
        If you want to add visual elements (like a scoreboard), you will want to add your 
        code between background() and the first call to translate().
        """
        background(0,0,0)  
        
        
        text("Moves: %d" %self.counter, 450, 50)
        fill(255,255,255)
        
        translate(WIDTH//2- (len(self.grid[0])//2)*CELL_SIZE, HEIGHT//2- (len(self.grid)//2)*CELL_SIZE)        
        
        for row in self.grid:
            for tile in row:
                pushMatrix()
                translate(tile.x*CELL_SIZE, tile.y*CELL_SIZE)
                tile.draw()
                popMatrix()
                
        
        

    
   
    def keyPressed(self):
        """
        This is an event handler that responds to keys being typed by the user.
        
        This is setup so that the arrow keys control the player's movements and the 'n' and 
        'p' keys can be used to visit different levels.
        
        After handling key events, this should check if the level has been completed and 
        advance to the next level if it has.
        """
             
             
        if key.code == UP: #UP arrow
            self.player.move('N')
            self.counter+=1
        elif key.code == DOWN: #DOWN arrow
            self.player.move('S')
            self.counter+=1
        elif key.code == RIGHT: #RIGHT arrow
            self.player.move('E')
            self.counter+=1
        elif key.code == LEFT: #LEFT arrow
            self.player.move('W')
            self.counter+=1
        elif key.char in 'nN' and self.level < self.MAX_LEVEL:
            self.level += 1
            self.loadLevel()
            self.counter=0
        elif key.char in 'pP' and self.level > 0:
            self.level -= 1
            self.loadLevel()
            self.counter=0
        elif key.char in 'rR':
            self.loadLevel()
            self.counter=0
        # Check whether the level is complete here
        if game.levelComplete() == True:
            game.level += 1
            game.loadLevel()
            self.counter=0
        
      
    

        
if __name__ == '__main__':
    """
    This makes this collection of classes into an actual application. 
    It creates a new game board and hooks up the event handlers.
    """
    frameRate(30)
    size(WIDTH, HEIGHT)
    game = SokobanBoard()
    draw = lambda: game.draw()
    keyPressed = lambda: game.keyPressed()

    run()
        
    