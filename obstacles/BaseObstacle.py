import pygame
from pygame.sprite import Sprite
from config import WHITE, PLAYER_SIZE

class BaseObstacle(Sprite):
    def __init__(self, screen, color, x, y, **kwargs ):

        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([PLAYER_SIZE, PLAYER_SIZE])
        self.image.fill(color)
        # Set our transparent color
        self.image.set_colorkey(WHITE)
        self.original_image = self.image

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.angle = 0

    def update(self):

        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.screen.blit(self.image, (self.x, self.y))
