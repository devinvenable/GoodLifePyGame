import pygame
from player_objects.BasePlayer import Player
from config import PLAYER_SIZE

# Devin's work goes here

class Player1(Player):
    def __init__(self, screen, color, x, y, **kwargs ):

        Player.__init__(self, screen, color, x, y, **kwargs)

        # use this line to load an image for your player if you don't want to use the default square
        self.original_image = pygame.image.load("images/phoenix_stage5.png").convert()

        # Use scale to scale image to fit your rect
        self.original_image = pygame.transform.scale(self.original_image, (PLAYER_SIZE, PLAYER_SIZE))

        # In my case, I want to horizontally flip my image so that the front of my car moves in the right direction.
        self.original_image = pygame.transform.flip(self.original_image, True, True)

        self.image = self.original_image



