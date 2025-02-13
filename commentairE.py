import random, json

class commentairE:
    def __init__(self):
        self.dictionnairE = json.load(open("dictionnairE.json", 'r'))
    def esTtUuNmoTdElAlanguEfrancaisE(self, s):
        return self.dictionnairE.get(s.lower())!=None

    def esTtUuNcommentairEvalidE(self, lexemE):
        lEcommentairE = lexemE.split(' ') 
        for i in range(len(lEcommentairE)):
            if not self.esTtUuNmoTdElAlanguEfrancaisE(lEcommentairE[i]):
                moTaleatoirE = list(self.dictionnairE.keys())[random.randint(0, len(self.dictionnairE.keys()))]
                print(f"J'ai rien compris écrit en français, ne voulais-tu pas écrire {moTaleatoirE} ")

c = commentairE()
c.esTtUuNcommentairEvalidE("grahou")