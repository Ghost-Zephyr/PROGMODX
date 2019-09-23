# -*- coding: utf-8 -*-

n = input("Navn: ")

try:
    a = int(input("Alder: "))
except ValueError:
    print("\n\033[31mAlderen må være et tall!\033[0m")

try:
    if 18 <= a:
        print(n, "er", a, "og kan kjøre bil med førerkort.")
    else:
        print(n, "er", a, "og kan ikke kjøre bil.")
except NameError:
    pass

