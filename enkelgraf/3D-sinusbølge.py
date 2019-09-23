# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:32:26 2019

@author: Sivert
"""

import matplotlib.pyplot as plt
import math

fig = plt.figure()
ax = fig.gca(projection='3d')

def sineWave(ix, iy, iz):
    x, y, z = [], [], []
    for i in range(iz, iz+30):
        x.append(i+ix)
        y.append(iy)
        z.append(math.sin(i+ix)*7.5+iz)
    return (tuple(x), tuple(y), tuple(z))


x1, y1, z1 = sineWave(0, 0, 0)
x2, y2, z2 = sineWave(15, 0, 15)


ax.plot(x1, y1, z1, label='Sine Wave 1')
ax.plot(x2, y2, z2, label='Sine Wave 2')
ax.legend() # Infoboks øverst til høyre

plt.show()

