import pygame
from player_objects.Player1 import Player1
from player_objects.Player2 import Player2
from player_objects.Player3 import Player3
from player_objects.Player4 import Player4
from player_objects.Player5 import Player5
from player_objects.Player6 import Player6
from obstacles.Bomb import Bomb

from config import (RED, BLACK, GREEN, BLUE, BLUE_GREEN, YELLOW, PURPLE,
                    SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_SIZE)

pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("GoodLife")

sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = Player1(screen, RED, 0, 0, control=True)
sprites.add(player)

player = Player2(screen, YELLOW, SCREEN_WIDTH - PLAYER_SIZE, 0 )
sprites.add(player)

player = Player3(screen, BLUE, 0, (SCREEN_WIDTH-PLAYER_SIZE) / 2 )
sprites.add(player)

player = Player4(screen, BLUE_GREEN, 0, SCREEN_HEIGHT-PLAYER_SIZE)
sprites.add(player)

player = Player5(screen, PURPLE, SCREEN_WIDTH-PLAYER_SIZE, SCREEN_HEIGHT-PLAYER_SIZE)
sprites.add(player)

player = Player6(screen, PURPLE, SCREEN_WIDTH-PLAYER_SIZE, (SCREEN_HEIGHT-PLAYER_SIZE)/2)
sprites.add(player)

bomb = Bomb(screen, PURPLE, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
sprites.add(bomb)
enemies.add(bomb)

running = True
while running:

    # Get the events
    for event in pygame.event.get():

        # Quit if X button is pressed
        if event.type == pygame.QUIT:
            running = False

        ## Press ESC to exit game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill(BLACK)
    sprites.update()


    pygame.display.flip()

pygame.quit()
