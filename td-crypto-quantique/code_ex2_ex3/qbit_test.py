from qbit import Qbit

def test1():
    q = Qbit(0,0) # polarisation 0, value 0
    if(q.read(0) != 0): # lecture avec polarisation 0
        return False 
    return True

def test2():
    q = Qbit(0,1)# polarisation 0, value 1
    if(q.read(0) != 1): # lecture avec polarisation 0
        return False 
    return True

def test3():
    q = Qbit(1,0)# polarisation 1, value 0
    if(q.read(0) not in [0,1]): # lecture avec polarisation 0, value 1 ou zero
        return False 
    return True

def test4():
    q = Qbit(0,0)# polarisation 1, value 0
    if(q.read(1) not in [0,1]): # lecture avec polarisation 0, value 1 ou zero
        return False 
    return True

val = test1() and test2() and test3() and test4()
if(val):
    print("Tests PASSED")
else:
    print("Tests FAILED")