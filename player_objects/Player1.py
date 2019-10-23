import pygame
from player_objects.BasePlayer import Player
from config import PLAYER_SIZE

# Devin's work goes here

class Player1(Player):
    def __init__(self, screen, color, x, y, **kwargs ):

        Player.__init__(self, screen, color, x, y, **kwargs)

        # replace base image with loaded version
        self.original_image = pygame.image.load("images/phoenix_stage5.png").convert()
        self.original_image = pygame.transform.scale(self.original_image, (PLAYER_SIZE, PLAYER_SIZE))
        self.image = self.original_image


