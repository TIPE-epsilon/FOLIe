from analyseuR import *
from interpreteuR import *
from commentairE import *

fichieR = open(input("nom du fichier : "))
instancEDanalyseuR = analyseuR(fichieR)

chaoS = satisfactioN()
codE = instancEDanalyseuR.lecturEdElexemE()
instancEDanalyseuR.fermeRfichieR(fichieR)
interpreteR(codE, chaoS)
