import pygame
import time
import csv


WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Merge Hero")
TAN = (206,184,136)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
FPS = 60
GEM_SIZE = 50
colors = {'r':RED,'g': GREEN, 'b': BLUE, 'k': BLACK}

gem_grid = [['r','b','g','r','b','g'],
            ['b','g','r','b','g','r'],
            ['g','r','b','g','r','b'],
            ['r','b','g','r','b','g'],
            ['b','g','r','b','g','r'],
            ['g','r','b','g','r','b'],
            ]

new_gem_grid = gem_grid
select = False 
#Make sure to do something about this -> very bad style
with open('new_gem_grid.csv','w+',newline='') as gem_writer:
        mywriter = csv.writer(gem_writer, delimiter=',')
        mywriter.writerows(gem_grid)
from Gem import Gem

def create_gem_grid(new_gem_grid):
    list_of_gems = []
    for index, row in enumerate(new_gem_grid):
        row_of_gems = []
        for col_index, col in enumerate(row):
            if col == 0:
                row_of_gems.append(0)
            else:
                gem_color = col
                row_of_gems.append(Gem(gem_color,index,col_index))
                #row_of_gems[col_index].place_gem()
        list_of_gems.append(row_of_gems)
    return list_of_gems
#Initial array of gem objects
list_of_gems = create_gem_grid(new_gem_grid)
#print(list_of_gems)
def is_adjacent(gem1,gem2):
    gems = gem1 + gem2
    for pos in gems:
        if pos < 0:
            #print("Index less than zero")
            return False
    if gem1[0] >= len(list_of_gems) or gem2[0] >= len(list_of_gems):
        #print("Row index too large")
        return False
    if gem1[1] >= len(list_of_gems[0]) or gem2[1] >= len(list_of_gems[0]):
        #print("Column index too large")
        return False
    #Check to see if in same column
    if gem1[1] == gem2[1]:
        if gem1[0] + 1 == gem2[0] or gem1[0] - 1 == gem2[0]:
            #print("These are adjacent in the column")
            return True
    elif gem1[0] == gem2[0]:
        if gem1[1] + 1 == gem2[1] or gem1[1] - 1 == gem2[1]:
            #print("These are adjacent in the row")
            return True
    else:
        return False

def draw_gem_grid(list_of_gems):
    for index, row in enumerate(list_of_gems):
        for col_index, col in enumerate(row):
            if col != 0:
                list_of_gems[index][col_index].place_gem()

def switch_gems(gem1_pos, gem2_pos):
    global list_of_gems
    gem1_row = gem1_pos[0]
    gem1_col = gem1_pos[1]
    gem2_row = gem2_pos[0]
    gem2_col = gem2_pos[1]

    list_of_gems[gem1_row][gem1_col], list_of_gems[gem2_row][gem2_col] = list_of_gems[gem2_row][gem2_col], list_of_gems[gem1_row][gem1_col]
    #update with set new position
    list_of_gems[gem1_row][gem1_col].set_new_position(gem1_row,gem1_col)
    list_of_gems[gem2_row][gem2_col].set_new_position(gem2_row,gem2_col)

def click_action():
    if len(Gem.clicked_gems) == 2:
        gem1_pos = Gem.clicked_gems[0]
        gem2_pos = Gem.clicked_gems[1]
        gem1_row = gem1_pos[0]
        gem1_col = gem1_pos[1]
        gem2_row = gem2_pos[0]
        gem2_col = gem2_pos[1]
        if gem1_pos == gem2_pos:
            list_of_gems[gem1_row][gem1_col].deselect()
            Gem.clicked_gems = []
        elif not is_adjacent(gem1_pos, gem2_pos):
            Gem.clicked_gems.pop()
            list_of_gems[gem2_row][gem2_col].deselect()
        else:
            #move gems
            Gem.clicked_gems = []
            switch_gems(gem1_pos, gem2_pos)
            list_of_gems[gem1_row][gem1_col].deselect()
            list_of_gems[gem2_row][gem2_col].deselect()

def drop_gems():
    global list_of_gems
    #Start at the bottom and work up
    #print_gems()
    for row_index in range(len(list_of_gems)-1):
        for col_index in range(len(list_of_gems[0])):
            test_row = len(list_of_gems) - row_index - 1
            #print(f"row, col: {test_row}, {col_index}")
            if list_of_gems[test_row - 1][col_index] == 0:
                continue
            if list_of_gems[test_row][col_index] == 0 and list_of_gems[test_row - 1][col_index].is_moveable:
                #print("Zero found. Dropping tiles")
                #print(f"row, col: {test_row}, {col_index}")
                
                list_of_gems[test_row][col_index] = list_of_gems[test_row - 1][col_index]
                #print_gems()
                #time.sleep(1)
                list_of_gems[test_row - 1][col_index] = 0
                #print_gems()
                #time.sleep(1)
                list_of_gems[test_row][col_index].set_new_position(test_row,col_index)

def check_three_in_a_row():
    global list_of_gems
    def check_vertical():
        for row in range(len(list_of_gems)-2):
            for col in range(len(list_of_gems[0])):
                if list_of_gems[row][col] == 0:
                    continue
                if not list_of_gems[row][col].is_moveable:
                    continue
                try:
                    if list_of_gems[row][col].color == list_of_gems[row + 1][col].color and list_of_gems[row + 1][col].color == list_of_gems[row + 2][col].color:
                        for row_pos in range(row, row+3):
                            list_of_gems[row_pos][col] = 0
                        #print("Three in a row found vertically")
                except:
                    continue
    def check_horizontal():
        for row in range(len(list_of_gems)):
            for col in range(len(list_of_gems[0])-2):
                if list_of_gems[row][col] == 0:
                    continue
                if not list_of_gems[row][col].is_moveable:
                    continue
                try:
                    if list_of_gems[row][col].color == list_of_gems[row][col + 1].color and list_of_gems[row][col + 1].color == list_of_gems[row][col + 2].color:
                        for col_pos in range(col, col+3):
                            list_of_gems[row][col_pos] = 0
                        #print("Three in a row found horizontally")
                except:
                    continue
    
    check_vertical()
    check_horizontal()
            


def draw_window():
    global list_of_gems
    WIN.fill(TAN)
    base_rect = pygame.draw.rect(WIN, BLACK, pygame.Rect(50,450, 800, 25))
    #center_rect = pygame.draw.rect(WIN, BLACK, pygame.Rect(450, 0, 1, 500))
    draw_gem_grid(list_of_gems)
    pygame.display.update()

def select_gem(mouse, mouse_clicked):
    global select
    for index, row in enumerate(list_of_gems):
        for col_index, col in enumerate(row):
            if col == 0:
                continue
            button = pygame.Rect(col.get_gem_rect()) 
            if button.collidepoint(mouse) and mouse_clicked:
                select = True
            if select == True and not mouse_clicked and button.collidepoint(mouse):
                select = False
                col.select()
#print(Gem().clicked_gems)

def main():
    clock = pygame.time.Clock()
    run = True
    mouse_clicked = False
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_clicked = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_clicked = False
        mouse = pygame.mouse.get_pos()
        select_gem(mouse, mouse_clicked)
        click_action()
        check_three_in_a_row()
        drop_gems()
        draw_window()
        
    pygame.quit()

if __name__ == "__main__":
    main()
