# -*- coding: utf-8 -*-

import numpy as np

def cubeRoot(x):
     x = abs(x)
     return x ** (1. / 3)

try:
     V = float(input("Volum: "))
     r = cubeRoot((4*np.pi*V) / 3)

     print("En kule med Volum = {} vil ha Radius = {}".format(V, round(r, 3)))
     
except TypeError:
     print("Volumet må være et tall")

