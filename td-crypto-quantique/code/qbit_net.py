from random import randint
from qbit import Qbit
import socket, pickle


def randomQbit(sendValue, nb_pol):
    val = randint(0,1)
    sendValue.append(val)
    return Qbit(randint(0,nb_pol-1), val)

def qbit_observer(srcPort, dst, dstPort, NbQbits=1024, nb_pol = 2):
    so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    so.bind(('', srcPort))
    so.listen(1)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((dst, dstPort))

    client,_ = so.accept()

    for i in range(0, NbQbits):
        data = client.recv(63)
        q = pickle.loads(data)
        val = q.read(i%nb_pol)
        new_qbit = Qbit(randint(0,1), val)
        s.send(pickle.dumps(new_qbit))


    data = client.recv(NbQbits*4)
    s.send(data)

    so.close()
    s.close()


def client(dst, dstport, nbQbits=1024, nb_pol = 2):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((dst, dstport))
    sendValue = []

    for _ in range(0, nbQbits):
        q = randomQbit(sendValue, nb_pol)
        data = pickle.dumps(q)
        v = s.send(data)


    sendingByte = pickle.dumps(sendValue)
    s.send(sendingByte)

    s.close()

def qbit_server(srcport, NBQbit=1024, nb_pol = 2):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', srcport))
    s.listen(1)
    client,_ = s.accept()
    dataRead = []
    cpt = 0
    AliceData = []

    for _ in range(0, NBQbit):
        data = client.recv(63)
        q = pickle.loads(data)

        dataRead.append(q.read(cpt%nb_pol))

    data = client.recv(NBQbit*4)
    q = pickle.loads(data)
    AliceData = q


    # client.close()
    s.close()


    matchVal = 0
    cpt = 0
    for alice in AliceData:
        bob = dataRead[cpt]
        if(alice == bob):
            matchVal += 1
        cpt += 1

    print("Transmistion accuracy: {:.2f}%".format((matchVal*100)/NBQbit))