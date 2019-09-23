# -*- coding: utf-8 -*-

pt = []

try:
    print("Skriv inn sidene i trekanten:")
    for i in range(0, 3):
        pt.append(int(input(f"Side {str(i+1)}: ")))
except ValueError:
    print("Ikke et tall!")
    exit()

pt.sort()

a, b, c = pt

if a**2 + b**2 == c**2:
    print("Tallene er en Pytagorisk tripel!")
else:
    print("Tallene er ikke en Pytagorisk tripel!")

