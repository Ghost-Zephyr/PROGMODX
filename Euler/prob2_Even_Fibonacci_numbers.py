# -*- coding: utf-8 -*-

def nfibb(p, i):
    return i, p+i

p = 0
i = 1
a = [0]

while p+i < 4000000:
    p, i = nfibb(p, i)
    if i % 2 == 0:
        a.append(i)

sum = 0

for i in a:
    sum += i

print(sum)

