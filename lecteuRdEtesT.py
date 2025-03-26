from analyseuR import *
from interpreteuR import *
from commentairE import *

fichieR = open(input("nom du fichier : "))
instancEDanalyseuR = analyseuR(fichieR)

chaoS = satisfactioN()
codE = instancEDanalyseuR.lecturEdElexemE(chaoS)
instancEDanalyseuR.fermeRfichieR(fichieR)
interpreteR(codE, chaoS, desinsectificatioN=instancEDanalyseuR.fichieR)
