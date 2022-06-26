import sys
import socket
from _thread import *
import pickle
from player import Player

if len(sys.argv[1:]) == 2:
    server, port = sys.argv[1:]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((server, port))
    except socket.error as e:
        str(e)

    s.listen(2)
    print("Server Started. Waiting for a connection")

    connected = set()
    players = {}
    idCount = 0


    def threaded_client(conn, p, playerID):
        global idCount
        conn.send(str.encode(str(p)))

        reply = ""
        while True:
            try:
                data = conn.recv(4096).decode()

                if playerID in players:
                    game = players[playerID]

                    if not data:
                        break
                    else:
                        # if data == "reset":
                        #     game.resetWent()
                        # elif data != "get":
                        #     game.play(p, data)

                        conn.sendall(pickle.dumps(game))
                else:
                    break
            except:
                break

        print("Lost connection")
        try:
            del players[playerID]
            print("Closing Game", playerID)
        except:
            pass
        idCount -= 1
        conn.close()


    while True:
        conn, addr = s.accept()
        print("Connected to:", addr)

        idCount += 1
        p = 0
        playerID = (idCount - 1)//2
        if idCount > 4:
            players[playerID] = Player(playerID)
            print("Creating a new game...")
        else:
            players[playerID].ready = True
            p = 1


        start_new_thread(threaded_client, (conn, p, playerID))
else:
    print("Invalid Input !! ex. python server.py 192.168.0.100 8000")


