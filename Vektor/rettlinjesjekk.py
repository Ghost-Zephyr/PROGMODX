# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 00:31:06 2019

@author: siver
"""

import numpy as np
import matplotlib.pyplot as plt

# Leser inn tre punkter og konverterer til liste.
P1 = list(map(int, input("Tast inn punkt 1 <x y>:").split()))
P2 = list(map(int, input("Tast inn punkt 2 <x y>:").split()))
P3 = list(map(int, input("Tast inn punkt 3 <x y>:").split()))

v1 = np.array(P3) - np.array(P1)
v2 = np.array(P2) - np.array(P1)

if np.cross(v1, v2) == 0:
    print("Punktene {}, {} og {} ligger på en rett linje!".format(P1, P2, P3))
else:
    print("Punktene {}, {} og {} liggeer ikke på en rett linje!".format(P1, P2, P3))

plt.plot([P1[0], P2[0], P3[0]], [P1[1], P2[1], P3[1]], 'bo')
plt.ylabel('Y')
plt.xlabel('X')
plt.show()

