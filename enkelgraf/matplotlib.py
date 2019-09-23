# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:32:26 2019

@author: Sivert
"""

import matplotlib.pyplot as plt

x = (0, 1, 2, 3, 4)
y = (0, 1, 4, 9, 16)
z = (0, -1.5, 0, 4.51, 12.01)


plt.grid()
plt.xlabel('$x$') # Merker x-aksen
plt.ylabel('$f(x)$') # Merker y-aksen

plt.plot(x, y, 'bx-.', label='$f(x)=x^2$')
plt.plot(x, z, 'gs:', label='$f(x)=-3x+1.5x^2$')
plt.legend() # Infoboksen øverst i venstre hjørne
plt.show()
