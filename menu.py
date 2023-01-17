import pygame
import settings
from pygame.locals import *
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
        status = "Play"
    else:
        status = "Menu"
    return status
