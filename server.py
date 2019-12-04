import os
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)
players = {}

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
                           'x':x,
                           'y':y,
                           'r':r
                           }

    #print(players)
    others = {i: players[i] for i in players if i != player}
    #print(others)
    return jsonify(others)

if __name__ == "__main__":
    game_ip = os.getenv('GAME_IP', None)
    if game_ip:
        app.run(host='172.16.42.68')
    else:
        app.run()
