# -*- coding: utf-8 -*-

try:
    n = int(input("Primtall? "))
except ValueError:
    print("Ikke et tall!")
    exit()

prim = False

for i in range(2, n):
    if n/i == n//i:
        break
    elif i == n-1:
        prim = True

if prim:
    print("Ja")
else:
    print("Nei")

