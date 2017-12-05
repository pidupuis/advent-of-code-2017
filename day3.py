#!/usr/bin/python

from math import sqrt

p = 277678
n = int(sqrt(p) + 1)
c = int((n + 1) / 2)

steps = list(range(c-1, n-1))
steps = list(reversed(steps)) + steps[1:] + [n-1]

print(
    [steps[i % len(steps)] for i, v in enumerate(
        range(((n-2)**2)+1, (n**2)+1)
    ) if v == p][0]
)
