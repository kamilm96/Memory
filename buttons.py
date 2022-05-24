import pygame
pygame.init()
font = pygame.font.SysFont('Arial', 20)

class Button:
    def __init__(self, text, x, y, pos_x, pos_y, bg='grey'):
        self.x = x
        self.y = y
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.text = font.render(text, 1, pygame.Color('Black'))
        self.surface = pygame.Surface((self.x,self.y))
        self.surface.fill(bg)
        self.surface.blit(self.text, (self.x*0.25,self.y*0.25))
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.x, self.y)
        self.clicked = False
        
    def clicked_button(self,surface):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                print(str(self.text) + 'clicked')
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        surface.blit(self.surface, (self.pos_x,self.pos_y))
        return action