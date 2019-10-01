# -*- coding: utf-8 -*-

n = 2520
ar = []

while True:
    for i in range(1, 11):
        if (n / i) == (n // i):
            ar.append(i)
            break

a = n

for i in ar:
    if i < a:
        a = i

