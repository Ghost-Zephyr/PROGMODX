# -*- coding: utf-8 -*-

n = 0 #2520
a = 0

while True:
    for i in range(1, 11):
        if (n / i) == (n // i):
            a = n
            break
    i += 1

