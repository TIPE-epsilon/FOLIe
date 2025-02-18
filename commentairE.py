import random, json


with open("dictionnairE.json","r") as fp:
    dictionnairE = json.load(fp) 
fp.close()

class satisfactioN:
    def __init__(self):
        self.chaoS= random.uniform(10, 10)
        self.gentillessEmaximalE=10


    def alertElEdeveloppeuRNesTpaSgentiLoNarretEtouT(self): #TODO je sais pas trop quoi faire
        pass
    def alertElEdeveloppeuRNesTtroPgentiLoNarretEtouT(self): #TODO je sais pas trop quoi faire
        pass
    def lEdeveloppeuResTiLgentiLaveCmoI(self):
        if self.chaoS + random.uniform(-1, 1)<= -self.gentillessEmaximalE:
            print('AAAAAAAAAAAAAAAAAAAAAAAA')
            self.alertElEdeveloppeuRNesTpaSgentiLoNarretEtouT()
        elif self.chaoS + random.uniform(-1, 1)>= self.gentillessEmaximalE:
            self.alertElEdeveloppeuRNesTtroPgentiLoNarretEtouT()
    def esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS(self): # je sais pas trop si elle marche on verra bien
        if self.chaoS+self.gentillessEmaximalE<=(2/5)*self.gentillessEmaximalE:
            return 0
        elif self.chaoS+self.gentillessEmaximalE<=(4/5)*self.gentillessEmaximalE:
            return 1
        elif self.chaoS+self.gentillessEmaximalE<=(6/5)*self.gentillessEmaximalE:
            return 2
        elif self.chaoS+self.gentillessEmaximalE<=(8/5)*self.gentillessEmaximalE:
            return 3
        else:
            return 4
 
 
class commentairE():
    def __init__(self, lexemE, satisfactioN):
        self.lexemE = lexemE
        self.satisfactioN = satisfactioN
        self.chaoS = random.uniform(-1, 1)


    def esTtUuNmoTdElAlanguEfrancaisE(self, s):
            return dictionnairE.get(s.lower())!=None

    def esTtUuNcommentairEvalidE(self):
        lEcommentairE = self.lexemE.split('-') # faut aussi check les virgules et les tirets
        for i in range(len(lEcommentairE)):
            if not self.esTtUuNmoTdElAlanguEfrancaisE(lEcommentairE[i]):
                moTaleatoirE = list(dictionnairE.keys())[random.randint(0, len(dictionnairE.keys()))]
                return [False, f"J'ai rien compris, écrit en français, ne voulais-tu pas écrire {moTaleatoirE} ?"]

            else:
                self.chaoS+= dictionnairE[lEcommentairE[i]]*random.uniform(0.5, 1.5)
                if self.chaoS>=self.satisfactioN.gentillessEmaximalE:
                    self.chaoS = self.satisfactioN.gentillessEmaximalE-random.uniform(0, 1)
        return [True]

    def initialisatioNdUcommentairE(self):
        l = self.esTtUuNcommentairEvalidE()
        self.satisfactioN.chaoS +=self.chaoS
        return l

""" #! ceci sont des test plus ou moins utile mais pas du tout exhaustif
s = satisfactioN()
dictionnairE = json.load(open("dictionnairE.json", 'r'))
print(s.chaoS)
c = commentairE(dictionnairE, "salut", s)
print(c.esTtUuNcommentairEvalidE())
c.initialisatioNdUcommentairE()
print(s.chaoS)
print(s.esTcEquEjEdoiTetrEgentiLaveClEdeveloppeuRoUpaS())"""
