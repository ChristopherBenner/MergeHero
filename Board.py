import pygame
from Gem import Gem
import menu
import level as level
import time
score = 0
new_gem_grid = [[0,0,0],[0,0,0],[0,0,0]]
select = False

def set_new_gem_grid(gem_grid):
    global new_gem_grid, list_of_gems, score
    Gem.new_gem_grid = gem_grid
    new_gem_grid = gem_grid
    score = 0
    list_of_gems = create_gem_grid(new_gem_grid)
    draw_gem_grid(list_of_gems)

def create_gem_grid(new_gem_grid):
    global list_of_gems
    list_of_gems = []
    for index, row in enumerate(new_gem_grid):
        row_of_gems = []
        for col_index, col in enumerate(row):
            if col == 0:
                row_of_gems.append(0)
            else:
                gem_color = col
                row_of_gems.append(Gem(gem_color,index,col_index))
        list_of_gems.append(row_of_gems)
    return list_of_gems

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
    global score
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
            score += 1
            list_of_gems[gem1_row][gem1_col].deselect()
            list_of_gems[gem2_row][gem2_col].deselect()
    return score

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
                    if list_of_gems[row][col].is_moving or list_of_gems[row + 1][col].is_moving or list_of_gems[row + 2][col].is_moving:
                        continue
                    elif list_of_gems[row][col].color == list_of_gems[row + 1][col].color and list_of_gems[row + 1][col].color == list_of_gems[row + 2][col].color:
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
                    if list_of_gems[row][col].is_moving or list_of_gems[row][col+ 1].is_moving or list_of_gems[row][col + 2].is_moving:
                        continue
                    elif list_of_gems[row][col].color == list_of_gems[row][col + 1].color and list_of_gems[row][col + 1].color == list_of_gems[row][col + 2].color:
                        for col_pos in range(col, col+3):
                            list_of_gems[row][col_pos] = 0
                        #print("Three in a row found horizontally")
                except:
                    continue
    
    check_vertical()
    check_horizontal()
            
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
def check_win():
    for row in range(len(list_of_gems)):
        for col in range(len(list_of_gems[0])):
            if list_of_gems[row][col] == 0:
                continue
            if list_of_gems[row][col].is_moveable:
                return False
    return True

def get_stars(current_level, level_score):
    stars = level.levels[current_level-1].get_star_moves()
    if level_score <= stars[0]:
        print("You won three stars")
        stars_earned = 3
    elif level_score <= stars[1]:
        print("You won two stars")
        stars_earned = 2
    elif level_score <= stars[2]:
        print("You won one star")
        stars_earned = 1
    else:
        print("You won zero stars")
        stars_earned = 0
    level.levels[current_level-1].stars_earned = stars_earned

def play_level(mouse, mouse_clicked, status):
    global level_score
    if status == "Play":
        status = menu.restart(mouse, mouse_clicked, status)
    select_gem(mouse, mouse_clicked)
    level_score = click_action()
    check_three_in_a_row()
    drop_gems()
    level_won = check_win()
    status = menu.draw_menu_button(mouse, mouse_clicked, status)
    draw_gem_grid(list_of_gems)

    return status, level_score