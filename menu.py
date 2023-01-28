import pygame
import settings
from pygame.locals import *
import time
import level as level
WIDTH, HEIGHT = settings.WIDTH, settings.HEIGHT
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 40)
text = font.render("Start", True, (255,255,255), None)
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
status = "Menu"
max_level = level.get_max_level()

def draw_start_menu():
    background_image = pygame.image.load("images\menu_background.png")
    start_button = pygame.image.load("images\Start.png")
    WIN.blit(background_image,(0,0))
    WIN.blit(start_button,(WIDTH/2 - 50, HEIGHT/2 + 100))
    pygame.display.update()
def check_start_clicked(mouse, mouse_clicked):
    button = pygame.Rect(WIDTH/2 - 50, HEIGHT/2 + 100, 100, 50) 
    if button.collidepoint(mouse) and mouse_clicked:
        status = "Select Level"
    else:
        status = "Menu"
    return status
def draw_menu_button(mouse, mouse_clicked, status):
    menu_button_background = pygame.image.load("images/menu.png")
    WIN.blit(menu_button_background, (75,75))
    menu_button = pygame.Rect(75, 75, 100, 50)
    if menu_button.collidepoint(mouse) and mouse_clicked:
        status = "Menu"
    return status
def restart(mouse, mouse_clicked, status):
    play_level_background = pygame.image.load("images/play_background.png")
    WIN.blit(play_level_background,(0,0))
    restart_button_background = pygame.image.load("images/restart.png")
    WIN.blit(restart_button_background, (750,75))
    restart_button = pygame.Rect(750, 75, 75, 75)
    if restart_button.collidepoint(mouse) and mouse_clicked:
        status = "Restart"
    return status
def draw_select_level(mouse, mouse_clicked, max_level_unlocked):
    count = 0
    button_height = 100
    button_width = 100
    #level_buttons = []
    background_image = pygame.image.load("images/basic_background.png")
    WIN.blit(background_image,(0,0))
    level_button_image = pygame.image.load("images/level_button.png")
    level_rects = {}
    for column in range(5):
        for row in range(3):
            count += 1
            if count <= max_level_unlocked:
                x_placement = 100 + 150* column
                y_placement = 90 + 125 * row
                level_rects["level" + str(count)] = (count,(100 + 150* column, 90 + 125* row, button_width, button_height))
                #draw_stars(count, x_placement, y_placement)
            else:
                break

    for level, rect in level_rects.items():
        WIN.blit(level_button_image,(rect[1][0],rect[1][1]))
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("Level " + str(rect[0]), True, (255,255,255), None)
        text_rect = text.get_rect()
        text_rect.center = (rect[1][0] + button_width/2, rect[1][1] + button_height /2)
        #WIN.blit(text, (rect[1][0] + button_width/5, rect[1][1] + button_height/3))
        WIN.blit(text,text_rect)
        draw_stars(rect[0], rect[1][0], rect[1][1])
        #level_buttons.append(button)
        #Add a way to place the stars achieved
        click_button = pygame.Rect(rect[1])
        if click_button.collidepoint(mouse) and mouse_clicked:
            status = "Play"
            current_level = rect[0]
            time.sleep(1)
            break
        else:
            status = "Select Level"
            current_level = 0
        
    pygame.display.update()
    return status, current_level

def next_level(mouse, mouse_clicked, current_level, status):
    original_level = current_level
    background_image = pygame.image.load("images/basic_background.png")
    WIN.blit(background_image,(0,0))
    win_font = pygame.font.Font('freesansbold.ttf', 40)
    level_font = pygame.font.Font('freesansbold.ttf', 20)
    text = win_font.render(f"Congratulations, you won level {current_level}", True, (255,255,255), None)
    text_rect = text.get_rect()
    text_rect.center = (WIDTH/2, HEIGHT/2)
    WIN.blit(text, text_rect)

    #Next Level Button
    next_level = pygame.image.load("images/next_level.png")
    WIN.blit(next_level,(675,350))
    next_level_button = pygame.Rect(700, 350, 100, 50)
    
    #Replay Level Button
    replay_level = pygame.image.load("images/replay.png")
    WIN.blit(replay_level,(75,350))
    replay_level_button = pygame.Rect(75, 350, 150, 50)
    if next_level_button.collidepoint(mouse) and mouse_clicked:
        current_level += 1
        status = "Play"
        #print("Next Level")
    elif replay_level_button.collidepoint(mouse) and mouse_clicked:
        status = "Play"
        #print("Replay")
    else:
        status = "Next Level"
    status = draw_menu_button(mouse, mouse_clicked, status)
    draw_stars_big(original_level)
    pygame.display.update()
    return status, current_level
def draw_stars(count, x_placement, y_placement):
    stars_earned = level.levels[count-1].stars_earned
    grey_star = pygame.image.load("images/grey_star.png")
    grey_star = pygame.transform.scale(grey_star,(15,15))
    gold_star = pygame.image.load("images/gold_star.png")
    gold_star = pygame.transform.scale(gold_star,(15,15))
    star_color = grey_star
    for star in range(3):
        y_pos = y_placement + 65
        x_pos = x_placement + star * 25 + 20
        if star < stars_earned:
            star_color = gold_star
        else:
            star_color = grey_star
        WIN.blit(star_color, (x_pos,y_pos))
        #star_display = pygame.draw.rect(WIN, (255,255,0), pygame.Rect(x_pos, y_pos, 15, 15))
    #pygame.display.update()

def draw_stars_big(original_level):
    stars_earned = level.levels[original_level-1].stars_earned
    grey_star = pygame.image.load("images/grey_star.png")
    gold_star = pygame.image.load("images/gold_star.png")
    star_color = grey_star
    for star in range(3):
        y_pos = 100
        x_pos = 325 + 100 * star
        if star < stars_earned:
            star_color = gold_star
        else:
            star_color = grey_star
        WIN.blit(star_color, (x_pos,y_pos))
        #star_display = pygame.draw.rect(WIN, color, pygame.Rect(x_pos, y_pos, 75,75))
    #pygame.display.update()



def game_over(mouse, mouse_clicked):
    status = "Game Over"
    status = draw_menu_button(mouse, mouse_clicked, status)
    background_image = pygame.image.load("images/basic_background.png")
    WIN.blit(background_image,(0,0))
    win_font = pygame.font.Font('freesansbold.ttf', 40)
    text = win_font.render(f"Congratulations, you won the game!", True, (255,255,255), None)
    text_rect = text.get_rect()
    text_rect.center = (WIDTH/2, HEIGHT/2)
    WIN.blit(text, text_rect)
    pygame.display.update()
    return status

    
    

def main():
    clock = pygame.time.Clock()
    run = True
    mouse_clicked = False
    level_selected = True
    current_level = 1
    FPS = 60
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
        #draw_select_level(mouse, mouse_clicked)
        next_level(mouse, mouse_clicked, current_level)
        #print(f"Current status: {status}")

if __name__ == "__main__":
    main()