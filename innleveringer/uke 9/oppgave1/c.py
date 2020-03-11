# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt

collatz = lambda x: x*3 + 1 if x % 2 else x/2

lolpts = []

for i in range(2,10**6): #10**7-1):
    n = i
    it = 0
    while n != 1:
        n = collatz(n)
        it += 1
    lolpts.append((i, it))

xl = [x for x, y in lolpts]
yl = [y for x, y in lolpts]

plt.scatter(xl, yl, s=1)

