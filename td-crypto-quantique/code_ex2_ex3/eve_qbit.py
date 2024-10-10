from constant import *
from random import randint
from qbit import Qbit
import socket, pickle

host = "localhost"

def randomQbit():
    return Qbit(randint(0,1), randint(0,1))

so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
so.bind(('', PORT))
so.listen(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, EVE_PORT))

client,_ = so.accept()
dataRead = []
cpt = 0
AliceData = []

for _ in range(0, NB_QBITS):
    data = client.recv(63)
    q = pickle.loads(data)
    val = q.read(cpt%2)
    new_qbit = Qbit(randint(0,1), val)
    s.send(pickle.dumps(new_qbit))
    

data = client.recv(NB_QBITS*4)
s.send(data)

so.close()
s.close()