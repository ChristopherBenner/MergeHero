import pygame
import new_gem_grid
#Help! I don't want to have to call all of these variables
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
GEM_SIZE = 50
#new_gem_grid =[]
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
FPS = 60
GEM_SIZE = 50
colors = {'r':RED,'g': GREEN, 'b': BLUE, 'k': BLACK}
'''with open('new_gem_grid.csv','r') as gem_reader:
    reader = csv.reader(gem_reader)
    new_gem_grid = list(reader)'''
#Initial gem_grid
'''gem_grid = [['r','b','g','r','b','g'],
            ['b','g','r','b','g','r'],
            ['g','r','b','g','r','b'],
            ['r','b','g','r','b','g'],
            ['b','g','r','b','g','r'],
            ['g','r','b','g','r','b'],
            ]
'''
new_gem_grid = [[0,0,0],[0,0,0],[0,0,0]]
#new_gem_grid = []
#new_gem_grid = new_gem_grid.get_new_gem_grid()
class Gem():
    #global new_gem_grid, colors
    global colors
    new_gem_grid = [[0,0,0],[0,0,0],[0,0,0]]
    new_gem_grid = []
    clicked_gems = []
    def __init__(self, color, grid_row, grid_column): #Color should be passed as a single letter since it makes the 
                                                    #grid easier to see what lines up
        self.color = color
        if self.color == 'k':
            self.is_moveable = False
            self.is_selectable = False
        else:
            self.is_moveable = True
            self.is_selectable = True
        self.gem_x, self.gem_y = self.set_new_position(grid_row,grid_column, new_gem_grid)
        self.clicked = False
        self.selected = False
    

    def set_new_position(self, grid_row, grid_column,new_gem_grid = [[0,0,0],[0,0,0],[0,0,0]]):
        #Top of base rect is at 450 px
        #Place each gem at 450 - (GEM_SIZE * (row_offset - self.row_pos)) for y pos
        #Place gem at 400 + GEM_SIZE* self.col_pos -> Change this to center after working
        self.row_pos = grid_row
        self.col_pos = grid_column
        try:
            row_offset = len(new_gem_grid)
            column_offset = len(new_gem_grid[0])
        except:
            row_offset = 0
            column_offset = 0
        self.new_position_x = 450 + GEM_SIZE * self.col_pos - (column_offset/2 * GEM_SIZE)
        self.new_position_y = 450 - (GEM_SIZE *(row_offset - self.row_pos))

        return self.new_position_x, self.new_position_y

    def place_gem(self):
        self.move_gem()
        pygame.draw.rect(WIN,colors[self.color],pygame.Rect(self.gem_x, self.gem_y,GEM_SIZE,GEM_SIZE))
        if self.selected == True:
            pygame.draw.rect(WIN,(255,255,0),pygame.Rect(self.gem_x, self.gem_y,GEM_SIZE,GEM_SIZE),5)

    def get_gem_rect(self):
        return (self.gem_x,self.gem_y, GEM_SIZE,GEM_SIZE)

    def get_gem_grid_pos(self):
        return (self.row_pos,self.col_pos)

    def move_gem(self):
        #move the gem to the new position
        move_x = 10
        move_y = 10
        #self.new_position_x = 100
        #self.new_position_y = 0
        #Edit this some more to make it smoother
        if self.new_position_x == self.gem_x and self.new_position_y == self.gem_y:
            self.is_moving = False
        else:
            self.is_moving = True
        if self.new_position_x > self.gem_x +10: 
            self.gem_x += move_x
        elif self.new_position_x < self.gem_x - 10:
            self.gem_x -= move_x
        elif self.new_position_y > self.gem_y + 10:
            self.gem_y += move_y
        elif self.new_position_y < self.gem_y - 10:
            self.gem_y -= move_y
        else:
            self.gem_x = self.new_position_x
            self.gem_y = self.new_position_y

    def select(self):
        if self.is_selectable:
            #print(f"Gem at pos {self.row_pos},{self.col_pos} selected")
            self.clicked_gems.append((self.row_pos,self.col_pos))
            self.selected = True
            #print(f"Here is the list of gems that have been clicked: {self.clicked_gems}")
            self.clicked = True

    def deselect(self):
        self.selected = False
        self.clicked = False
        self.place_gem()