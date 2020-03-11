# -*- coding: utf-8 -*-

try:
    kroppsvekt = int(input("\nKroppsvekt i kg: "))
except ValueError:
    print("\nIkke et tall!")
    exit(420)

vann = kroppsvekt * 15 / 100

print(f"En person på {kroppsvekt}kg, kommer til å dø etter å ha mistet {vann}kg vann")

