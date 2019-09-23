# -*- coding: utf-8 -*-

try:
    kroppsvekt = int(input("Kroppsvekt i kg: "))
except ValueError:
    print("Ikke et tall!")

vann = kroppsvekt * 15 / 100

print("En person på {}kg, kommer til å dø etter å mistet {}kg vann".format(kroppsvekt, vann))

