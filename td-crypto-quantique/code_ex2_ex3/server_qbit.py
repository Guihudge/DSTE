from constant import *
from random import randint
from qbit import Qbit
import socket, pickle

host = "localhost"

def randomQbit():
    return Qbit(randint(0,1), randint(0,1))

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', EVE_PORT))
socket.listen(1)
client,_ = socket.accept()
dataRead = []
cpt = 0
AliceData = []

for _ in range(0, NB_QBITS):
    data = client.recv(63)
    q = pickle.loads(data)
    
    dataRead.append(q.read(cpt%2))

data = client.recv(NB_QBITS*4)
q = pickle.loads(data)
AliceData = q


client.close()
socket.close()


matchVal = 0
cpt = 0
for alice in AliceData:
    bob = dataRead[cpt]
    if(alice == bob):
        matchVal += 1
    cpt += 1

print("Transmistion accuracy: {:.2f}%".format((matchVal*100)/NB_QBITS))
