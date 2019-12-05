# -*- coding: utf-8 -*-

navn = "Sivert V. Sæther"
adresse = "Romolslia 33c"
tlf = "98465910"

print("\nNavn: {}\nAdresse: {}\nTelefon: {}\n\nOg disse variablene er strenger (strings):\n{}".format(
        navn, adresse, tlf, {"navn":type(navn),"adresse":type(adresse),"tlf":type(tlf)}))
