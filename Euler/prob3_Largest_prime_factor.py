# -*- coding: utf-8 -*-

n = 600851475143
a = []

for i in range(2, n + 1):
    if(n % i == 0):
        isprime = 1
        for j in range(2, (i //2 + 1)):
            if(i % j == 0):
                isprime = 0
                break
        if (isprime == 1):
            a.append(i)

l = 0

for i in a:
    if i > l:
        l = i

