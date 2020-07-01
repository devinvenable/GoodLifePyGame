import pygame
from config import WHITE, PLAYER_SIZE
from player_objects.BasePlayer import Player

class Player3(Player):
    def __init__(self, screen, color, x, y, **kwargs ):

        Player.__init__(self, screen, color, x, y, **kwargs)

        # use this line to load an image for your player if you don't want to use the default square
        self.original_image = pygame.image.load("images/cum_hat.jpg").convert()

        # Use scale to scale image to fit your rect
        self.original_image = pygame.transform.scale(self.original_image, (PLAYER_SIZE, PLAYER_SIZE))

        # In my case, I want to horizontally flip my image so that the front of my car moves in the right direction.
        self.original_image = pygame.transform.flip(self.original_image, False, False)

        self.image = self.original_image