import numpy as np
from math import *


pv = float(input("Pression de la vapeur en atm (P1): ")) #pv = pression de la vapeur d'eau en atm
psat = float(input("Pression saturante en atm (P2): ")) #psat = pression saturante de la vapeur d'eau en atm
tamb = float(input("Temperature ambiante en Kelvin (T1): ")) #tamb = temperature ambiante en Kelvin
dvap = 40.65 #dvap = enthalpie de vaporisation de l'eau
r = 8.31 # R en Pa.m3.mol-1.K-1
def clap_formula():
    #tdp = dew point temperature en Kelvin
    tdp = 1/(((np.log(pv/psat))*r/dvap)+(1/tamb))
    print(tdp)
clap_formula()
