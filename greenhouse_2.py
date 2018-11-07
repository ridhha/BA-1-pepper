"""
Entrées:
Flux Direct, Flux Indirect, Température souhaitée, conductivité thermique

Sortie:
Température du plastique, Température du sol, Puissance par mètre carré

But du programme:
Ce programme nous permet de trouver les différentes inconnues du bloc "Effet de Serre"
A l'aide d'une fonction utilisant le module "scipy", ce code nous permet de trouver nos inconnues
"""

"""Importation du module scipy.optimize"""
from scipy.optimize import fsolve

"""Cette fonction permet de résoudre un système de 3 équations à 3 inconnues
Les 3 inconnues sont: 1°Tplastique 2°Tsol 3°P"""
def systeme(variables):
    Tp = variables[0]
    Ts = variables[1]
    P = variables [2]
    f = [[0]*1]*3
    f[0] = h * ((Tp - T) + (Ts - T)) - P
    f[1] = P + (s * (Tp**4)) - Fd - Fi
    f[2] = (s * (Ts**4)) + (h * (Ts-T)) - Fd - (s * (Tp**4))
    return f

"""Initialisation des inconnues"""
Tp, Ts, P = 0, 0, 0
inconnues = [Tp, Ts, P]

"""Inputs"""
Fd = float(input("Fd = "))
Fi = float(input("Fi = "))
T = float(input("T = "))
s = 5.6697e-8
# A comprendre:
l = 1
H = 0.1
a = 27e-6
g = 9.81
µ = 1.91e-5
c = 29e-3 #conductivité thermique de l'air
b = 1/(273.15+65)
Dt = 37
Ray = ((H**3)*b*g*Dt)/(a*µ)
h = ((c)*(0.4)*((Ray)**(1/4)))/H

"""Résolution du problème"""
solutions_Bloc3 = fsolve(systeme, inconnues)
print(solutions_Bloc3)