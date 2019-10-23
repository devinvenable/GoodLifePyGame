import pygame
from config import WHITE
from player_objects.BasePlayer import Player

# Devin's work goes here

class Player1(Player):
    def __init__(self, screen, color, x, y ):
       Player.__init__(self, screen, color, x, y)

       self.image = pygame.image.load("../images/player.png").convert()

    def update(self):
        Player.update(self)
