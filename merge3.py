import pygame
import time
import csv
from Gem import Gem
import Board
import level as level
import settings
import menu

WIDTH, HEIGHT = settings.WIDTH, settings.HEIGHT
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
current_level = 1
level_selected = True
status = "Menu"

def draw_window(mouse,mouse_clicked):
    global list_of_gems, status, current_level, level_selected
    WIN.fill(TAN)
    base_rect = pygame.draw.rect(WIN, BLACK, pygame.Rect(50,450, 800, 25))
    #Add options for picking a level, win screen after each level, final win screen
    if status == "Menu":
        menu.draw_start_menu()
        status = menu.check_start_clicked(mouse, mouse_clicked)
        if status == "Select Level":
            mouse_clicked = False
            time.sleep(0.5)
    elif status == "Select Level":
        #time.sleep(1)
        status, current_level = menu.draw_select_level(mouse, mouse_clicked)
        if status == "Play":
            level_selected = True
    elif status == "Play":
        if level_selected and current_level <= level.get_max_level():
            new_gem_grid = level.get_gem_grid(current_level)
            Board.set_new_gem_grid(new_gem_grid)
            level_selected = False
        Board.play_level(mouse, mouse_clicked)
        level_won = Board.check_win()
        if level_won:
            print("Congratulations, you won")
            status = "Select Level"
            time.sleep(0.1)
        else:
            status = "Play"
        #print(status)
    pygame.display.update()
def main():
    clock = pygame.time.Clock()
    run = True
    mouse_clicked = False
    level_selected = True
    current_level = 1
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
        #move this section to if status == Select Level
        
        
        
        #level_won = Board.check_win()
        #if level_won:
        #status = "Select Level"
        

        draw_window(mouse, mouse_clicked)
        
    pygame.quit()

if __name__ == "__main__":
    main()
