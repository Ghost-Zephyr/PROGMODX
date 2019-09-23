# -*- coding: utf-8 -*-

found = False
a = []
p = []

for i in range(0, 100):
    for j in range(0, 10):
        a.append((999-i, 999-j))

for t in a:
    i = str(t[0] * t[1])
    if i == i[::-1]:
        p.append(i)

p.sort(reverse=True)

print(p[0])

