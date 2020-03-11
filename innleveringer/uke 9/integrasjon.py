# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np

def rekt(f, a, b, N, ax=False, offset=0.5):
    #rects = []
    S = 0
    dx = (b-a)/N
    
    if ax:
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        #ax.title('Rektangelmetoden:')
        ax.plot([a,b], [0,0], color='blue')
        x = np.linspace(a, b, 100)
        ax.plot(x, f(x), color='red', label='f(x)')
    
    for n in range(N):
        x = a + n*dx
        h = f(x + offset*dx)
        A = dx*h
        #rects.append(A)
        S += A
        if ax:
            ax.plot([x,x], [0,h], color='blue')
            ax.plot([x+dx,x+dx], [0,h], color='blue')
            ax.plot([x,x+dx], [h,h], color='blue')
    
    return S#, rects

def trap(f, a, b, N, ax=False):
    #traps = []
    S = 0
    dx = (b-a)/N
    
    if ax:
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        #ax.title('Rektangelmetoden:')
        ax.plot([a,b], [0,0], color='blue')
        x = np.linspace(a, b, 100)
        ax.plot(x, f(x), color='red', label='f(x)')
    
    for n in range(N):
        x = a + n*dx
        h = f(x + dx)
        A = dx*(h + f(x))/2
        #traps.append(A)
        S += A
        if ax:
            ax.plot([x,x], [0,f(x)], color='blue')
            ax.plot([x+dx,x+dx], [0,h], color='blue')
            ax.plot([x,x+dx], [f(x),h], color='blue')
    
    return S#, traps

if __name__ == '__main__':
    #f = lambda x: np.sin(x)
    #f = lambda x: x**3 - 2*x**2 + 4*x -1
    f = lambda x: x**2 - x + 4
    
    #integralsum = rekt(f, 0, 3, 8, plt.figure().add_subplot(111))
    integralsum = rekt(f, 3, 7, 40, plt.figure().add_subplot(111), 0.5)
    print(f'Sum av integralet er: {integralsum}')
    
    integralsum = trap(f, 3, 7, 40, plt.figure().add_subplot(111))
    print(f'''Sum av integralet er: {integralsum}''')

