import pygame
import sys

pugame.init()


screen = pygame.display.set_mod((800,600))
clock = pygame.time.Clock()
pygame.display.set_caption("Menu")
font = pygame.font.Font(None. 36)

menu_options = ["Start","Setting","Exit"]
select_option = 0



fps = 30
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0 ,0)
GREEN = (0, 555, 0)

Class Buttion:
def __init__ (self, text, x ,y , width, height, color, hover_color):
  self.text = text


def draw(self, screen):
  mouse_pos = pygame.moyse.get_pos()
  if self.x < moyse_pos[0] < self.x + self.width  \
  pygame.draw.rect(screen, self.hover_color,(self.x, self.y, self.width, self.height))
else:
  pygame.draw.rect(screen, self.color,(self.x, , self.y, self.width, self.height)
  text = font.render(self.text , True, WHITE)
  text_rect = text.get_rect(
    center = self.x + self.width / 2 self.y +self.height / 2)
  screen.blit(text, text_rect)

buttons = []
fot i, option in enumerate(menu_optuons):
  buttons = Buttons(option,400 , -100 ,200  + i
