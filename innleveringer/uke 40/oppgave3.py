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

kassabeholdning = {
    "kronestykke": 5,
    "femkrone": 5,
    "tikrone": 5,
    "tjuekrone": 5,
    "femtilapp": 5,
    "hundrelapp": 5,
    "tohundrelapp": 5,
    "femhundrelapp": 5,
    "tusenlapp": 5,
}

def vekslepenger(pris, betalt):
    if betalt < pris:
        print(f"Mangler {pris-betalt}kr!")
        return
    veksel = []
    vt = 0
    while betalt - vt > pris:
        for k, v in sorted(valor.items(), key=itemgetter(1), reverse=True):
            if betalt - vt - v >= pris:
                vt += v
                veksel.append(k)
    print(f"{vt} tilbake:")
    for p in veksel:
        print(p)

def uttak(belop):
    vt = 0
    while vt < belop:
        for k, v in sorted(valor.items(), key=itemgetter(1), reverse=True):
            while vt + v <= belop:
                if kassabeholdning[k] < 1:
                    break
                vt += v
                kassabeholdning[k] -= 1
        if vt < belop:
            print("Not enough veksel!")
            break
    return kassabeholdning

def innskudd():
    try:
        inp = str(input("Hvor mange av hva? "))
        inp = inp.split(" ")
        kassabeholdning[inp[1]] += int(inp[0])
    except:
        print("Wrong usage of innskudd!")

def kassa(kassabeholdning):
    try:
        inp = str(input("Kassa på Rimi: "))
        inp = inp.split(" ")
        cmd, args = inp[0], inp[1:]
        if cmd == "uttak":
            kassabeholdning = uttak(int(args[0]))
        elif cmd == "innskudd":
            innskudd()
        elif cmd == "vekslepenger":
            vekslepenger(int(args[0]), int(args[1]))
        elif cmd == "kassabeholdning":
            for k, v in kassabeholdning.items():
                print(f"{k}: {v}")
        elif cmd == "exit":
            raise KeyboardInterrupt
        else:
            print("Bare innskudd, uttak, vekslepenger og kassabeholdning er støttet!")
        kassa(kassabeholdning)
    except KeyboardInterrupt:
        print("Stopping Kassa")
    except:
        print("Kassa encountered an error!")
        kassa(kassabeholdning)

print("Rimi kassa, type exit and hit enter or CTRL+C to quit.")
try:
    kassa(kassabeholdning)
except KeyboardInterrupt: pass

