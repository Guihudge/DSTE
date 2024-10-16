import qbit_net, asyncio, time, threading

def start_back(func):
    background = threading.Thread(target=func)
    background.start()

def bob():
    qbit_net.qbit_server(4242)

def alice(alicePort):
    qbit_net.client("localhost", alicePort)

def eve():
    qbit_net.qbit_observer(4343, "localhost", 4242)

def oscar():
    qbit_net.qbit_observer(4444, "localhost", 4343)

print("Without observer")
start_back(bob)
alice(4242)

time.sleep(0.5)
print("With 1 observer")
start_back(bob)
time.sleep(0.2)
start_back(eve)
time.sleep(0.2)
alice(4343)

time.sleep(0.5)
print("With 2 observer")
start_back(bob)
time.sleep(0.2)
start_back(eve)
time.sleep(0.2)
start_back(oscar)
time.sleep(0.2)
alice(4444)