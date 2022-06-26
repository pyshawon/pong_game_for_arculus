# PONG GAME FOR ARCULUS

<img src="https://i.ibb.co/R3mHhzb/screenshot.png"/>

#### Requirements
- [Python3](https://docs.python.org/3/)
- [PyGame](https://www.pygame.org/docs/)


### Installation & Run

```bash
$ git clone https://github.com/pyshawon/pong_game_for_arculus.git

$ cd pong_game_for_arculus
$ virtualenv -p python3 env
$ source env/bin/activate
$ pip install -r requirements.txt

# To run the game with 4 player without network (Single Client)
$ python main.py

# TO PLAY THE GAME
# Keyboard Shortcuts
Move Left Paddle - (a, z)
Move Right Paddle - (k, m)
Move Top Paddle - (w, e)
Move Bottom Paddle - (o, p)
Reset Score - (r)
Exit Game - (q)

# Game will automatically over when any of 4 player score is equal to 20.
```

### Network Capabilities

```bash
# Network server is build but not connected with the Pong Game.

- server.py
- network.py
- client.py

# To Run the server

#python server.py <network_ip> <port>
$ python server.py 192.168.0.101 8000

```

### TODO
- Connect game engine to socket server.
- Integrating unit test.
- Better angle calculation when ball hits the paddle.
- Split code into more files for simplicity.


### PERSONAL NOTES
- I'm was not familiar with any game engine before today.
- I had to spend couple hour with python game engine (PyGame) documentation & some blogs to understand the basics & build the game.
- In short amount of time I couldn't figure it out better way to connect socket into game engine.



### THANK YOU