import pygame
from pygame.sprite import Sprite
from config import WHITE, PLAYER_SIZE
import random, math

class BaseObstacle(Sprite):
    def __init__(self, screen, color, x, y, **kwargs ):

        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.color = color

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
        self.dir_count = 0

    def update_movement(self ):

        #self.dir_count += 1
        #if self.dir_count >= 10:
        self.angle += random.randint(1,100) % 360
        print(self.angle)
        radians = math.radians(self.angle)
        y = self.y + (self.speed * math.cos(radians))
        x = self.x + (self.speed * math.sin(radians))

        if y + PLAYER_SIZE <= SCREEN_HEIGHT and y >= 0:
            self.y = y
        if x + PLAYER_SIZE <= SCREEN_WIDTH and x >= 0:
            self.x = x

    def update(self):

        self.update_movement()
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.screen.blit(self.image, (self.x, self.y))
