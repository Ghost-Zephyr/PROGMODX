# -*- coding: utf-8 -*-

from operator import itemgetter

valor = {
    "kronestykke": 1,
    "femkrone": 5,
    "tikrone": 10,
    "tjuekrone": 20,
    "femtilapp": 50,
    "hundrelapp": 100,
    "tohundrelapp": 200,
    "femhundrelapp": 500,
    "tusenlapp": 1000,
}

def vekslepenger(pris, betalt):
    if betalt < pris:
        print(f"Mangler {pris-betalt}kr!")
        return
    v = []
    vt = 0
    while betalt - vt > pris:
        for k, v in sorted(valor.items(), key=itemgetter(1), reverse=True):
            if betalt - vt - v >= pris:
                vt += v
                v.append(k)
                print(k)
    for p in v:
        print(p)

try:
    vekslepenger(420, 500)
except KeyboardInterrupt: pass

