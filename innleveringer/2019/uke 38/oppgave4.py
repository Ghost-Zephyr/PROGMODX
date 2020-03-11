# -*- coding: utf-8 -*-

a = []

try:
    n = int(input("Tall som skal faktorisereses: "))
except ValueError:
    print("Ikke et tall!")
    exit()

for i in range(2, n + 1):
    if(n % i == 0):
        isprime = 1
        for j in range(2, (i //2 + 1)):
            if(i % j == 0):
                isprime = 0
                break
        if (isprime == 1):
            a.append(i)

a.sort(reverse=True)

print("\nTallets faktorer:")

for i in a:
    print(i)

