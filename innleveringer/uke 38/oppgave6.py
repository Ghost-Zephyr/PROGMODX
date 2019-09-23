# -*- coding: utf-8 -*-

def fibb(n):
    if n <= 2:
        return 1
    else:
        return fibb(n-1)+fibb(n-2)

try:
    n = int(input("Fibonacci n: "))
except ValueError:
    print("Ikke et tall!")
    exit()

print(f"\nFibonacci(n) = {fibb(n)}\nn = {n}")

