# -*- coding: utf-8 -*-

pris = 850
strb = 25
tips = 10

try:
    pers = int(input("Hvor mange skal spise? "))
except:
    print("Nummer. Hvor MANGE skal spise?")

pris = pris - pris * strb / 100 # student rabatt

pris = pris + pris * tips / 100 # pluss tips

print("Måltidet koster {}kr pr. pers.".format(pris / pers))

