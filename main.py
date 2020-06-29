import pygame
import os
import requests
from player_objects.Player1 import Player1
from player_objects.Player2 import Player2
from player_objects.Player3 import Player3
from player_objects.Player4 import Player4
from player_objects.Player5 import Player5
from player_objects.Player6 import Player6
from obstacles.Bomb import Bomb
from config import (RED, BLACK, GREEN, BLUE, BLUE_GREEN, YELLOW, PURPLE, ORANGE,
                    SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_SIZE)

pygame.init()


pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("GoodLife")

sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
others  = pygame.sprite.Group()

player = Player1(screen, RED, 0, 0  )
sprites.add(player)

player = Player2(screen, ORANGE, SCREEN_WIDTH - PLAYER_SIZE, 0)
sprites.add(player)

player = Player3(screen, BLUE, 0, (SCREEN_WIDTH-PLAYER_SIZE) / 2)
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

def get_player(name):
    # This function will return a player from the sprites list with matching name
    return [x for x in sprites if x.id()==name][0]

# Get active player from env variable
aplayer = os.getenv('ACTIVE', 'Player3')
active_player = get_player(aplayer)
active_player.control=True

for s in sprites:
    if s.id() != active_player.id():
        others.add(s)



# Get server IP from env variable
#game_ip = os.getenv('GAME_IP', None)
#if game_ip:
#    server = f'http://{game_ip}:5000'
#else:
server = None

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

    screen.fill(ORANGE)
    sprites.update()

    pygame.display.flip()

    remote_check += 1

    if server and (remote_check % 1==0):
        remote_check=0
        params = data={'player': active_player.id(),
                       'x': active_player.x,
                       'y': active_player.y,
                       'r': active_player.angle,
                       }
        result = requests.get( server, params )
        if result:
            try:
                others = result.json()
                for k, v in others.items():
                    print('here', k, v)
                    pl = get_player(k)
                    pl.x = float(v['x'])
                    pl.y = float(v['y'])
                    pl.angle = float(v['r'])
            except:
                print(result.text)

    clock.tick(30)

pygame.quit()
