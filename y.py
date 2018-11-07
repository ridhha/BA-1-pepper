import numpy as np
from math import *

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

fd = float(input("fd : "))
fi = float(input(fi : ))
T = float(input("t : "))

def
