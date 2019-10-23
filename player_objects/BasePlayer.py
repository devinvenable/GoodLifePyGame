import pygame
from pygame.sprite import Sprite
from config import WHITE, PLAYER_SIZE

class Player(Sprite):
    def __init__(self, screen, color, x, y ):

        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        # Create an image of the block, and fill it with a color.

        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([PLAYER_SIZE, PLAYER_SIZE])
        self.image.fill(color)
        # Set our transparent color
        self.image.set_colorkey(WHITE)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        self.screen.blit(self.image, (self.x, self.y))
