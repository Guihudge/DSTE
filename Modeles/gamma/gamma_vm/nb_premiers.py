import random
from gemmaVM import *

def R(mol1:Molecule, mol2:Molecule):
    return mol1.getValue("v") % mol2.getValue("v") == 0

def A(reactif, mol1:Molecule, mol2:Molecule):
    reactif.remove(mol2)

n = 30  
initialState = [Molecule({"v": i}) for i in range(2, n+1)]

print("Initial State")
for m in initialState:
    print(m.getValue('v'), ", ", end="")

g = GemmaProgram(initialState, [R], [A])
g.run()

print("Prime Numbers:")
for m in g.getRactif():
    print(m.getValue("v"), end=" ")
print("")
