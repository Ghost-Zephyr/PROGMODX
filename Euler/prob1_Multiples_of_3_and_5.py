# -*- coding: utf-8 -*-

def inarray(i, a):
    try:
        a.index(i)
        return True
    except ValueError:
        return False

a = []
i = 0

while i*3 < 1000:
    if i*3 < 1000 and not inarray(i*3, a):
        a.append(i*3)
    if i*5 < 1000 and not inarray(i*5, a):
        a.append(i*5)
    i += 1

sum = 0

for m in a:
    sum += m

print(sum)
