import pygame
import time
import csv
from Gem import Gem
import Board
import level as level
import settings
import menu
import math

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
max_level_unlocked = 1
max_level = level.get_max_level()
level_score = 0
hero_position = [50,370] #x,y
hero_step_position = 1
#load the walk animation for the hero
hero_steps = []
hero_step_count = 1
walk = False
reached_destination = False

background_music = pygame.mixer.music.load("sounds/background_music.mp3")
#switch_sound = pygame.mixer.Sound("sounds/switch.mp3")
pygame.mixer.music.play(-1)

for i in range(4):
    image = pygame.image.load("images/hero_right_" + str(i + 1) + ".png")
    hero_steps.append(image)

def set_hero_image():
    global status, walk, hero_step_count, hero_position, hero_step_position, reached_destination
    if walk:
        step_delay = 5
        hero_step_count += 1

        if hero_step_count >= 4 * step_delay:
            hero_step_count = 1
        hero_step_position = math.floor(hero_step_count / step_delay) +1
        hero_position[0] += 5
    if hero_position[0] >= 700:
        #status = "Next Level"
        walk = False
        hero_position[0] = 50
        reached_destination = True
        time.sleep(0.8)
    else:
        reached_destination = False
    WIN.blit(hero_steps[hero_step_position -1], (hero_position[0],hero_position[1]))
    #return status


def draw_window(mouse,mouse_clicked):
    global status, current_level, level_selected, max_level_unlocked, level_score, walk
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
        status, current_level = menu.draw_select_level(mouse, mouse_clicked, max_level_unlocked)
        if status == "Play":
            level_selected = True
    elif status == "Next Level":
        status, current_level = menu.next_level(mouse, mouse_clicked, current_level, status)
        if status == "Play":
            level_selected = True
    elif status == "Game Over":
        status = menu.game_over(mouse, mouse_clicked)
    elif status == "Restart":
        level_selected = True
        status = "Play"
        time.sleep(0.1)
    elif status == "Play":
        if level_selected and current_level <= level.get_max_level():
            new_gem_grid = level.get_gem_grid(current_level)
            Board.set_new_gem_grid(new_gem_grid)
            level_selected = False
        
        level_won = Board.check_win()
        if level_won and not reached_destination:
            #status = "Play"
            walk = True
        if level_won and current_level <= max_level and not walk:
            print("Congratulations, you won")
            print(f"You took {level_score} moves")
            Board.get_stars(current_level, level_score)
            status = "Next Level"
            #status = "Walk"
            if current_level == max_level_unlocked and current_level < max_level:
                max_level_unlocked += 1
                print(f"Max level increased to {max_level_unlocked}")
            time.sleep(0.1)
        elif level_won and current_level >= max_level:
            status = "Game Over"
        else:
            #status = "Play"
            status, level_score = Board.play_level(mouse, mouse_clicked, status)
            set_hero_image()
    
    pygame.display.update()
def main():
    clock = pygame.time.Clock()
    run = True
    mouse_clicked = False
    level_selected = True
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

        draw_window(mouse, mouse_clicked)
        
    pygame.quit()

if __name__ == "__main__":
    main()
