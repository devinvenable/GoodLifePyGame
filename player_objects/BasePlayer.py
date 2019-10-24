import pygame, math
from pygame.sprite import Sprite
from config import WHITE, PLAYER_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT

class Player(Sprite):
    def __init__(self, screen, color, x, y, **kwargs ):

        print('kwargs', kwargs)
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        if 'control' in kwargs:
            self.control = True
            print('will control')
        else:
            self.control = False

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

    def update_movement(self ):
        radians = math.radians(self.angle)
        speed = 1
        y = self.y + (speed * math.cos(radians))
        x = self.x + (speed * math.sin(radians))

        if y + PLAYER_SIZE <= SCREEN_HEIGHT and y >= 0:
            self.y = y
        if x + PLAYER_SIZE <= SCREEN_WIDTH and x >= 0:
            self.x = x

    def update(self):

        if self.control:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_j] or pressed[pygame.K_LEFT]:
                if self.x >= 0:
                    self.x = self.x-1
            if pressed[pygame.K_l] or pressed[pygame.K_RIGHT]:
                if self.x + PLAYER_SIZE <= SCREEN_WIDTH:
                    self.x = self.x+1
            if pressed[pygame.K_i] or pressed[pygame.K_UP]:
                self.angle += 1 % 360
            if pressed[pygame.K_COMMA] or pressed[pygame.K_DOWN]:
                self.angle -= 1 % 360
            if pressed[pygame.K_SPACE]:
                self.update_movement()

        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.screen.blit(self.image, (self.x, self.y))
