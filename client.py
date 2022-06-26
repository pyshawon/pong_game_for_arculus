import pygame
import sys
from network import Network
import pickle
import random
from math import *

if len(sys.argv[1:]) == 2:
    server, port = sys.argv[1:]
    print(server)
    print(port)
else:
    print("Invalid Input !! ex. python client.py 192.168.0.100 8000")