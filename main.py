import pygame
import requests
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

player_control = Player1(screen, RED, 0, 0, )
sprites.add(player_control)

player = Player2(screen, YELLOW, SCREEN_WIDTH - PLAYER_SIZE, 0 )
sprites.add(player)

player = Player3(screen, BLUE, 0, (SCREEN_WIDTH-PLAYER_SIZE) / 2, control=True )
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

# We should only have one active, assumes this
active_player = [x for x in sprites if x.control==True][0]

# Set this to server, or None if you don't want to play with others
server = 'http://10.89.171.108:5000'

clock = pygame.time.Clock()

# Check once per every 60 frames for other player movement
remote_check = 0

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

    remote_check += 1

    if server and remote_check % 60:
        remote_check=0
        params = data={'player': active_player.id(), 'x': active_player.x, 'y': active_player.y}
        result = requests.get( server, params )
        if result:
            try:
                print(result.json())
            except:
                print(result.text)

    clock.tick(60)

pygame.quit()
