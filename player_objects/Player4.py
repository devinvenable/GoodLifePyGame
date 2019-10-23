import pygame
from config import WHITE
from player_objects.BasePlayer import Player

class Player4(Player):
    def __init__(self, screen, color, x, y ):
        Player.__init__(self, screen, color, x, y)

    def update(self):
        Player.update(self)
