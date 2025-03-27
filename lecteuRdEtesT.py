from analyseuR import *
from interpreteuR import *
from commentairE import *
import sys
sys.set_int_max_str_digits(2**(31)-1)
fichieR = open(input("nom du fichier : "))
instancEDanalyseuR = analyseuR(fichieR)

chaoS = satisfactioN()
codE = instancEDanalyseuR.lecturEdElexemE(chaoS)
instancEDanalyseuR.fermeRfichieR(fichieR)
interpreteR(codE, chaoS, desinsectisatioN=instancEDanalyseuR.fichieR)
