# -*- coding: utf-8 -*-

def collatzdef(x):
    if not x % 2:
        x = x*3 + 1
    else:
        x = x/2
    return x

collatz = lambda x: x*3 + 1 if not x % 2 else x/2

if __name__ == '__main__':
    n = 13
    i = 1
    print(f'n: {n}, iter: {i}')
    while n != 1:
        n = collatz(n)
        i += 1
        print(f'n: {n}, iter: {i}')

