# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np

derived = lambda f, x, h: (f(x+h) - f(x)) / h
symderived = lambda f, x, h: (f(x+h) - f(x-h)) / (2*h)

tad = np.loadtxt("vogn.txt", float, skiprows = 1)
times = []
dic = {}

f = lambda x: dic[x] #dic[float(x)]

for time, distance in tad:
    times.append(time)
    dic[time] = distance

syv, dyv = [[]]*2
la = times[0]
for time in times[1:-1]:
    ne = times[times.index(time)+1]
    #print(f'time: {time}, last: {la}, next: {ne}')
    syv.append(symderived(f, time, ne)) #, la))
    dyv.append(derived(f, time, ne))
    la = time

#x = np.linspace(times[1], times[-1], 1)
#syv = symderived(f, x, np.float(0.01))
#dyv = derived(f, x, 0.01)

plt.plot(times[1:-1], syv)
plt.plot(times[1:-1], dyv)



'''
if __name__ == '__main__':
    f = lambda x: np.sin(x)
    #f = lambda x: x**3 - 2*x**2 + 4*x -1
    
    x = np.linspace(0, 10, 125)
    sinx = f(x)
    derivedsinx = symderived(f, x, 1)
    
    plt.plot(x, sinx)
    plt.plot(x, derivedsinx)
'''
