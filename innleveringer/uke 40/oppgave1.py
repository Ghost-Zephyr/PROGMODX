# -*- coding: utf-8 -*-

try:
    sum = int(input("Sum: "))
except:
    print("Ikke et tall!")
    exit()
a = []

for i in range(2, sum + 1):
    if(sum % i == 0):
#        isprime = 1
#        for j in range(2, (i //2 + 1)):
#            if(i % j == 0):
#                isprime = 0
#                break
#        if (isprime == 1):
            a.append(i)

print(f"\nAlle primtall opp til {sum}:\n")

for i in a:
    print(i)


