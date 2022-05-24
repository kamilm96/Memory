import pygame
from pygame.locals import *
import buttons

pygame.init()
color = (99,241,188)
window = pygame.display.set_mode((800,600))
pygame.display.set_caption('Memory')
# pygame.display.set_icon(pygame.image.load('logo.png'))


def menu_start():
    new_game = buttons.Button('New game',150, 50, 150, 50)
    quit = buttons.Button('Quit', 150, 50, 150, 105)
    window.fill(color)
    # quit.clicked_button(window)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or quit.clicked_button(window):
                pygame.quit()
        if new_game.clicked_button(window):
            play_surface()
        pygame.display.update() 

def play_surface():
    window.fill(color)
    go_back = buttons.Button('Back', 150, 50, 350, 550)
    while True: 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        if go_back.clicked_button(window):
            menu_start()
        
        pygame.display.update()

menu_start()
play_surface()