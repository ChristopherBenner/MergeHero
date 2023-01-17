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

'''
gem_grid = [['r','b','g','r','b','g'],
            ['b','g','r','b','g','r'],
            ['g','r','b','g','r','b'],
            ['r','b','g','r','b','g'],
            ['b','g','r','b','g','r'],
            ['g','r','b','g','r','b'],
            ]
'''
#new_gem_grid = gem_grid
#new_gem_grid = level.get_gem_grid(current_level)

def draw_window(mouse,mouse_clicked):
    global list_of_gems
    WIN.fill(TAN)
    base_rect = pygame.draw.rect(WIN, BLACK, pygame.Rect(50,450, 800, 25))
    #center_rect = pygame.draw.rect(WIN, BLACK, pygame.Rect(450, 0, 1, 500))
    #draw_gem_grid(list_of_gems)
    Board.play_level(mouse, mouse_clicked)
    pygame.display.update()
def main():
    clock = pygame.time.Clock()
    run = True
    mouse_clicked = False
    level_selected = True
    current_level = 1
    status = "menu"
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
        
        if level_selected and current_level <= level.get_max_level():
            new_gem_grid = level.get_gem_grid(current_level)
            Board.set_new_gem_grid(new_gem_grid)
            level_selected = False
        level_won = Board.check_win()
        if level_won:
            level_selected = True
            current_level += 1
        

        draw_window(mouse, mouse_clicked)
        
    pygame.quit()

if __name__ == "__main__":
    main()
