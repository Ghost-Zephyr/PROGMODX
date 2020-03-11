# -*- coding: utf-8 -*-

def fibb(n):
    if n <= 2:
        return 1
    else:
        return fibb(n-1)+fibb(n-2)

print("This script calculates Fibbonacci(n)\n")

try:
    n = int(input("Fibonacci n: "))
    print(f"\nFibonacci({n}) = {fibb(n)}")
except ValueError:
    print("Ikke et tall!")
    exit()
except KeyboardInterrupt:
    print("Keyboard Interrupt beafore Fibbonaci sequence function finish!")



