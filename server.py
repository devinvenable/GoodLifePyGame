import os
from flask import Flask
from flask import request
from flask import jsonify
import math
import random

app = Flask(__name__)
players = {}

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
PLAYER_SIZE = 50
SPEED = 22


class bomb:
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    r = 0

    def __str__(self):
        return f"x is {self.x}, y is {self.y}, r is {self.r}"


bomb1 = bomb()
bomb2 = bomb()
bomb3 = bomb()


def update_movement(bomb):
    bomb.r += random.randint(1, 100) % 360
    print(bomb1.r)
    radians = math.radians(bomb.r)
    bomb.y = bomb.y + (SPEED * math.cos(radians))
    bomb.x = bomb.x + (SPEED * math.sin(radians))

    if bomb.y + PLAYER_SIZE <= SCREEN_HEIGHT and bomb.y >= 0:
        bomb.y = bomb.y
    if bomb.x + PLAYER_SIZE <= SCREEN_WIDTH and bomb.x >= 0:
        bomb.x = bomb.x
    if bomb.x <= 50:
        bomb.x = 50
    elif bomb.x >= 570:
        bomb.x = 570
    if bomb.y <= 50:
        bomb.y = 50
    elif bomb.y >= 570:
        bomb.y = 570
@app.route("/")
def hello():
    player = request.args.get('player', 'none')
    x = request.args.get('x', 'none')
    y = request.args.get('y', 'none')
    r = request.args.get('r', 'none')

    if player:
        if player in players.keys():
            p = players[player]
            print(p)
            if p['addr'] != request.remote_addr:
                return "Sorry, that player is already active"

        players[player] = {'addr': request.remote_addr,
                           'x': x,
                           'y': y,
                           'r': r
                           }

    # print(players)
    others = {i: players[i] for i in players if i != player}

    # Add in a bomb position
    update_movement(bomb1)
    update_movement(bomb2)
    update_movement(bomb3)

    others['Bomb1'] = {'addr': None,
                       'x': bomb1.x,
                       'y': bomb1.y,
                       'r': bomb1.r
                       }

    others['Bomb2'] = {'addr': None,
                       'x': bomb2.x,
                       'y': bomb2.y,
                       'r': bomb2.r
                       }

    others['Bomb3'] = {'addr': None,
                       'x': bomb3.x,
                       'y': bomb3.y,
                       'r': bomb3.r
                       }
    # print(others)
    return jsonify(others)


if __name__ == "__main__":
    # game_ip = os.getenv('GAME_IP', None)
    # if game_ip:
    #    app.run(host='192.168.0.73')
    # else:
    #    app.run()
    app.run(host='192.168.0.118')
