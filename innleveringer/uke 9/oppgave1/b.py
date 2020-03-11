# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt

collatz = lambda x: x*3 + 1 if x % 2 else x/2

collists = {
    '12': {'fig':plt.figure(),'l':[]},
    '19': {'fig':plt.figure(),'l':[]},
    '27': {'fig':plt.figure(),'l':[]},
    '5000': {'fig':plt.figure(),'l':[]}
}

print('''
This script calculates and shows values for each iteration
of collatz conjecture from a set of start values
''')

for n in collists:
    i = int(n)
    collists[n]['l'].append(i)
    while i != 1:
        i = collatz(i)
        collists[n]['l'].append(i)

i = 0

for n in collists:
    l = collists[n]
    ax = l['fig'].add_subplot(111)
    i += 1
    ax.plot(range(0, len(l['l'])), l['l'])
    ax.set_xlabel(f'collatz n = {n}')

