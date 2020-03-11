# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np

def rekt(f, a, b, N, ax=False, offset=0.5):
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
        S += A
        if ax:
            ax.plot([x,x], [0,h], color='blue')
            ax.plot([x+dx,x+dx], [0,h], color='blue')
            ax.plot([x,x+dx], [h,h], color='blue')
    
    return S

def trap(f, a, b, N, ax=False):
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
        S += A
        if ax:
            ax.plot([x,x], [0,f(x)], color='blue')
            ax.plot([x+dx,x+dx], [0,h], color='blue')
            ax.plot([x,x+dx], [f(x),h], color='blue')
    
    return S

dat = np.loadtxt("uke9/oppgave3/fallskjermmålinger.txt", float, skiprows = 1)

if __name__ == 'bajs':
    #f = lambda x: np.sin(x)
    #f = lambda x: x**3 - 2*x**2 + 4*x -1
    f = lambda x: x**2 - x + 4
    
    #integralsum = rekt(f, 0, 3, 8, plt.figure().add_subplot(111))
    integralsum = rekt(f, 3, 7, 40, plt.figure().add_subplot(111), 0.5)
    print(f'Sum av integralet er: {integralsum}')
    
    integralsum = trap(f, 3, 7, 40, plt.figure().add_subplot(111))
    print(f'''Sum av integralet er: {integralsum}''')

