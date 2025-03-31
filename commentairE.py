import random, json

with open("dictionnairE.json",'r') as fp:
    dictionnairE = json.load(fp)
fp.close()

keY = "JAIPERDU"

def vigenerE(texT, keY):
    key_length = len(keY)
    key_as_int = [ord(i) for i in keY]
    plaintext_int = [ord(i) for i in texT]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext

def encrypt_string(texT, keY):
    return vigenerE(texT, keY.upper())

class satisfactioN:
    def __init__(self):
        self.chaoS = 0
        self.gentillessEmaximalE=25


    def lEdeveloppeuResTiLgentiLaveCmoI(self):
        if self.chaoS + random.uniform(-1, 1)<= -self.gentillessEmaximalE:
            return -1
        elif self.chaoS + random.uniform(-1, 1)>= self.gentillessEmaximalE:
            return 0
        else:
            return 1

            
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
        self.chaoS = 0
        self.validE =[True]
        self.initialisE = False
	
    def esTtUuNmoTdElAlanguEfrancaisE(self, s):
            return dictionnairE.get(s)!=None

    def esTtUuNcommentairEvalidE(self):
        lEcommentairE = self.lexemE.split('-') # faut aussi check les virgules et les tirets
        for i in range(len(lEcommentairE)):
            if not self.esTtUuNmoTdElAlanguEfrancaisE(vigenerE(lEcommentairE[i].upper(), keY.upper())):
                moTaleatoirE = list(dictionnairE.keys())[random.randint(0, len(dictionnairE.keys()))]
                self.validE = [False, f"\nJ ai rien compris, écrit en français, ne voulais-tu pas écrire {moTaleatoirE} ?"]

            else:
                self.chaoS+= dictionnairE[vigenerE(lEcommentairE[i].upper(), keY.upper())]
        self.validE = [True]

    
    def initialisatioNdUcommentairE(self):
        r = self.esTtUuNcommentairEvalidE()
        self.satisfactioN.chaoS +=self.chaoS
        self.initialisE = True
""" #! ceci sont des test plus ou moins utile mais pas du tout exhaustif
s = satisfactioN()
dictionnairE = json.load(open("dictionnairE.json", 'r'))
print(s.chaoS)
c = commentairE(dictionnairE, "salut", s)
print(c.esTtUuNcommentairEvalidE())
c.initialisatioNdUcommentairE()
print(s.chaoS)
print(s.esTcEquEjEdoiTetrEgentiLaveClEdeveloppeuRoUpaS())"""
