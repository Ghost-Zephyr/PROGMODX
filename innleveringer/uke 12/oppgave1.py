#!/usr/bin/env python3
from math import e as econst

f = lambda x: econst**-x*(2*x**4-x-1)

def halvering(a, b, f, punkt):
    c = (a+b)/2
    while abs(f(c)) < punkt:
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
        c = (a+b)/2
    return c


