# -*- coding: utf-8 -*-

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

#valor.reverse()

def vekslepenger(pris, betalt):
    if betalt < pris:
        print(f"Mangler {pris-betalt}kr!")
    
    v = []
    vt = 0
    
    while betalt - vt > pris:
        for pv, i in enumerate(valor):
            if betalt - vt - int(pv) > pris:
                vt += int(pv)
                v.append(i)
                
    for p in v:
        print(p)


vekslepenger(420, 500)

