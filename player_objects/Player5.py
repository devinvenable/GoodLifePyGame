import pygame
from config import WHITE
from player_objects.BasePlayer import Player

class Player5(Player):
    def __init__(self, screen, color, x, y, **kwargs):
        Player.__init__(self, screen, color, x, y, **kwargs)

    def update(self ):
        Player.update(self)
