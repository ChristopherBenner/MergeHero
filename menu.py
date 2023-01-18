import pygame
import settings
from pygame.locals import *
import time
WIDTH, HEIGHT = settings.WIDTH, settings.HEIGHT
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 40)
text = font.render("Start", True, (255,255,255), None)
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
status = "Menu"

def draw_start_menu():
    WIN.fill((255,255,0))
    start_button = pygame.draw.rect(WIN, (0,0,255), pygame.Rect((WIDTH/2 - 50, HEIGHT/2 + 100, 100,50)))
    WIN.blit(text, (WIDTH/2 - 50, HEIGHT/2 + 100))
    pygame.display.update()
def check_start_clicked(mouse, mouse_clicked):
    button = pygame.Rect(WIDTH/2 - 50, HEIGHT/2 + 100, 100, 50) 
    if button.collidepoint(mouse) and mouse_clicked:
        status = "Select Level"
    else:
        status = "Menu"
    return status

def draw_select_level(mouse, mouse_clicked):
    count = 0
    button_height = 100
    button_width = 100
    #level_buttons = []
    level_rects = {}
    for column in range(5):
        for row in range(3):
            count += 1
            level_rects["level" + str(count)] = (count,(100 + 150* column, 90 + 125* row, button_width, button_height))

    for level, rect in level_rects.items():
        button = pygame.draw.rect(WIN, (127, 127, 127), pygame.Rect(rect[1]))
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("Level " + str(rect[0]), True, (255,255,255), None)
        text_rect = text.get_rect()
        text_rect.center = (rect[1][0] + button_width/2, rect[1][1] + button_height /2)
        #WIN.blit(text, (rect[1][0] + button_width/5, rect[1][1] + button_height/3))
        WIN.blit(text,text_rect)
        #level_buttons.append(button)
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
        draw_select_level(mouse, mouse_clicked)
        #print(f"Current status: {status}")

if __name__ == "__main__":
    main()