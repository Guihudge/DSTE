from constant import *
from random import randint
from qbit import Qbit
import socket, pickle

host = "localhost"

def randomQbit(sendValue):
    val = randint(0,1)
    sendValue.append(val)
    return Qbit(randint(0,1), val)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, PORT))
sendValue = []

for _ in range(0, NB_QBITS):
    q = randomQbit(sendValue)
    data = pickle.dumps(q)
    v = socket.send(data)
    

sendingByte = pickle.dumps(sendValue)
socket.send(sendingByte)

socket.close()
# print(sendValue)



