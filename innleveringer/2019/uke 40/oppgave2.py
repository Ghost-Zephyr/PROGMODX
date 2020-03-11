# -*- coding: utf-8 -*-

lag = "Rosenborg Molde Brann Strømsgodset Ålesund Lillestrøm Ranheim"
tippeligaen = []

def listeHåndtering(lag):
    t = lag.split(" ")
    for l in t:
        if l not in tippeligaen:
            tippeligaen.append(l)
    tippeligaen.sort()
    return tippeligaen

def opprykk(tippelag, oboslag):
    for i, l in enumerate(tippeligaen):
        if l == tippelag:
            tippeligaen[i] = oboslag
    #tippeligaen.sort()
    return tippeligaen

tippeligaen = listeHåndtering(lag)

print(tippeligaen)

tippeligaen = opprykk("Rosenborg", "Start")

print(tippeligaen)

