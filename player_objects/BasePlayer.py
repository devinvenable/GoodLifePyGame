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
        self.initial_x = self.x = x
        self.initial_y = self.y = y
        self.angle = 0
        self.rect = pygame.Rect((self.x, self.y),(PLAYER_SIZE, PLAYER_SIZE))
        self.speed = 24

    def id(self):
        return type(self).__name__

    def respawn(self):
        self.x = self.initial_x
        self.y = self.initial_y
        self.rect = pygame.Rect((self.x, self.y), (PLAYER_SIZE, PLAYER_SIZE))
        self.image = pygame.transform.rotate(self.original_image, 0)

    def update_movement(self ):
        radians = math.radians(self.angle)
        y = self.y + (self.speed * math.cos(radians))
        x = self.x + (self.speed * math.sin(radians))

        if y + PLAYER_SIZE <= SCREEN_HEIGHT and y >= 0:
            self.y = y
        if x + PLAYER_SIZE <= SCREEN_WIDTH and x >= 0:
            self.x = x

    def update(self):

        if self.control:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_j] or pressed[pygame.K_LEFT]:
                if self.x >= 0:
                    self.x = self.x-self.speed
            if pressed[pygame.K_l] or pressed[pygame.K_RIGHT]:
                if self.x + PLAYER_SIZE <= SCREEN_WIDTH:
                    self.x = self.x+self.speed
            if pressed[pygame.K_i] or pressed[pygame.K_UP]:
                self.angle += self.speed % 360
            if pressed[pygame.K_COMMA] or pressed[pygame.K_DOWN]:
                self.angle -= self.speed % 360
            if pressed[pygame.K_SPACE]:
                self.update_movement()

            self.rect = pygame.Rect((self.x, self.y), (PLAYER_SIZE, PLAYER_SIZE))

            from main import enemies, others
            if pygame.sprite.spritecollide(self, enemies, False):
                self.respawn()

            #if pygame.sprite.spritecollide(self, others, False):
            #    print('hit something')

        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.screen.blit(self.image, (self.x, self.y))

