import pygame
from player_objects.BasePlayer import Player
#from obstacles import BaseObstacle
from config import PLAYER_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH
import math, random

class Bomb(Player):
    def __init__(self, screen, color, x, y, **kwargs ):

        Player.__init__(self, screen, color, x, y, **kwargs)

        # replace base image with loaded version
        self.original_image = pygame.image.load("images/bomb.gif").convert()
        self.original_image = pygame.transform.scale(self.original_image, (PLAYER_SIZE, PLAYER_SIZE))
        self.image = self.original_image
        self.count_target = random.randint(1,300)
        self.counter = 0
        self.speed = 22


    def update(self):

        self.counter += 1
        if self.counter >= self.count_target:

            #self.update_movement()

            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.rect = pygame.Rect((self.x, self.y), (PLAYER_SIZE, PLAYER_SIZE))
            self.screen.blit(self.image, (self.x, self.y))

