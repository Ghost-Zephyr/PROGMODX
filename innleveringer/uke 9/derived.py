# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np

derived = lambda f, x, h: (f(x+h) - f(x)) / h # Newtons kvotinent
symderived = lambda f, x, h: (f(x+h) - f(x-h)) / (2*h) # Newtons symmetriske kvotinent

if __name__ == '__main__':
    f = lambda x: np.sin(x)
    #f = lambda x: x**3 - 2*x**2 + 4*x -1
    
    x = np.linspace(0, 10, 125)
    sinx = f(x)
    derivedsinx = derived(f, x, 1)
    
    plt.plot(x, sinx)
    plt.plot(x, derivedsinx)

