# -*- coding: utf-8 -*-

import numpy as np

def omkrets(r):
    O = np.pi * r
    print("Omkrets:", round(O, 2))
    return O

def areal(r):
    A = omkrets(r)**2
    print("Areal:", round(A, 2))
    return A

def volum(r):
    V = 4/3 * np.pi * r**3
    print("Volum:", round(V, 2))
    return V

try:
    r = int(input("Radius: "))
except ValueError:
    print("Ikke et tall!")

areal(r)
volum(r)

