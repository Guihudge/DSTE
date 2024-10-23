from gemmaVM import *
import random

def R(mol1:Molecule, mol2:Molecule):
    return mol1.getValue("i") == mol2.getValue("i")

def A(reactif, mol1:Molecule, mol2:Molecule):
    i = mol1.getValue("i")
    v = mol1.getValue("v") + mol2.getValue("v")
    reactif.remove(mol1)
    reactif.remove(mol2)
    reactif.append(Molecule({"i":i, "v":v}))


VectSize = 10
Vect1 = [ random.randint(0,30) for _ in range(VectSize)]
Vect2 = [ random.randint(0,30) for _ in range(VectSize)]

initialState = []

for i in range(VectSize):
    initialState.append(Molecule({"i":i, "v":Vect1[i]}))
    initialState.append(Molecule({"i":i, "v":Vect2[i]}))

g = GemmaProgram(initialState, [R], [A])
g.run()
result = g.getRactif()

s = [0,0,0,0,0,0,0,0,0,0]

for m in result:
    m:Molecule = m
    i = m.getValue("i")
    v = m.getValue("v")
    s[i] = v

print(Vect1)
print(Vect2)
print(s)
    
