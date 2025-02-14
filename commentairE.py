import random, json

class satisfactioN:
    def __init__(self):
        self.chaoS= random.uniform(-1, 1)


    def alertElEdeveloppeuRNesTpaSgentiLoNarretEtouT(self): # cette fontion est là, pour le moment
        pass

    def lEdeveloppeuResTiLgentiLaveCmoI(self):
        if self.chaoS + random.uniform(-1, 1)<= -self.gentillessEmaximalE:
            print('AAAAAAAAAAAAAAAAAAAAAAAA')
            self.alertElEdeveloppeuRNesTpaSgentiLoNarretEtouT()
        elif self.chaoS + random.uniform(-1, 1)>= -self.gentillessEmaximalE:
            print(":)")




class commentairE():
    def __init__(self, dictionnairE, lexemE, satisfactioN):
        self.dictionnairE = dictionnairE
        self.lexemE = lexemE
        self.satisfactioN = satisfactioN
        self.chaoS = random.uniform(-1, 1)
        self.gentillessEmaximalE=2


    def esTtUuNmoTdElAlanguEfrancaisE(self, s):
        return self.dictionnairE.get(s.lower())!=None

    def esTtUuNcommentairEvalidE(self):
        lEcommentairE = self.lexemE.split('-') # faut aussi check les virgules et les tirets
        for i in range(len(lEcommentairE)):
            if not self.esTtUuNmoTdElAlanguEfrancaisE(lEcommentairE[i]):
                moTaleatoirE = list(self.dictionnairE.keys())[random.randint(0, len(self.dictionnairE.keys()))]
                return [False, f"J'ai rien compris, écrit en français, ne voulais-tu pas écrire {moTaleatoirE} ?"]

            else:
                self.chaoS+= self.dictionnairE[lEcommentairE[i]]*random.uniform(0.5, 1.5)
                if self.chaoS>=self.gentillessEmaximalE:
                    self.chaoS = self.gentillessEmaximalE-random.uniform(0, 1)
        return 

    def initialisatioNdUcommentairE(self):
        l = self.esTtUuNcommentairEvalidE()
        self.satisfactioN.chaoS +=self.chaoS
        return l

    

s = satisfactioN()
dictionnairE = json.load(open("dictionnairE.json", 'r'))
print(s.chaoS)
c = commentairE(dictionnairE, "bonjour comment allez vous", s)
c.initialisatioNdUcommentairE()
print(s.chaoS)