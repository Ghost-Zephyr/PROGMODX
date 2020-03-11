# -*- coding: utf-8 -*-

collatz = lambda x: x*3 + 1 if x % 2 else x/2

while 'må være tall':
    try:
        inp = int(input('Collatz n: '))
        if inp > 0: break
        else: raise ValueError
    except ValueError:
        print('Got to be a positive numer!')

n = inp
i = 0

while n != 1:
    n = collatz(n)
    i += 1

print(f'Collatz conjecture of {inp} took {i} iterations to reach 1')

