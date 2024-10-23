import itertools

class Molecule:
    embded = {}
    alive = True
    def __init__(self, values:dict):
        self.embded = values
    
    def checkKey(self, key:str):
        return key in self.embded
    
    def getValue(self, key:str):
        if not self.checkKey(key):
            raise ValueError("Key not found")
        elif not self.alive:
            raise ValueError("Molecule is dead")
        else:
            return self.embded[key]
    
    def killMolecule(self):
        self.alive = False


class GemmaProgram:
    reactif = []
    predicats = []
    actions = []

    def __init__(self, initialstate, predicats, actions):
        self.reactif = initialstate
        self.predicats = predicats
        self.actions = actions

    def checkPredicat(self, mol1:Molecule, mol2:Molecule, predicat):
        return predicat(mol1, mol2)
    
    def action(self, mol1:Molecule, mol2:Molecule, action):
        action(self.reactif, mol1, mol2)
    
    def run(self):
        reaction = True
        gen = 0
        while reaction:
            reaction = False
            gen+= 1
            
            for subset in itertools.combinations(self.reactif, 2):
                mol1,mol2 = subset

                c = 0
                for p in self.predicats:
                    if(self.checkPredicat(mol1, mol2, p) and mol1 in self.reactif and mol2 in self.reactif):
                        self.action(mol1, mol2, self.actions[c])
                        reaction = True
                    if(self.checkPredicat(mol2, mol1, p) and mol1 in self.reactif and mol2 in self.reactif):
                        self.action(mol1, mol2, self.actions[c])
                        reaction = True
                        
                    c+=1
        print("finish in {} gens".format(gen))

    def getRactif(self):
        return self.reactif




