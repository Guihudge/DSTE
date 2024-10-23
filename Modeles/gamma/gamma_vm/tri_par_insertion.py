import random
from gemmaVM import *

def R(mol1:Molecule, mol2:Molecule):
    return mol1.getValue("i") < mol2.getValue("i") and mol1.getValue("v") > mol2.getValue("v")

def A(reactif, mol1:Molecule, mol2:Molecule):
    reactif.append(Molecule({"i":mol1.getValue("i"), "v":mol2.getValue("v")}))
    reactif.append(Molecule({"i":mol2.getValue("i"), "v":mol1.getValue("v")}))
    reactif.remove(mol1)
    reactif.remove(mol2)


VectSize = 10
Vect1 = [ random.randint(0,30) for _ in range(VectSize)]
initialState = []

for i in range(VectSize):
    initialState.append(Molecule({"i":i, "v":Vect1[i]}))

print(Vect1)

g = GemmaProgram(initialState, [R], [A])
g.run()

s = [0,0,0,0,0,0,0,0,0,0]

print("Final State")
for m in g.getRactif():
    i = m.getValue("i")
    v = m.getValue("v")
    s[i] = v

print(s)
