#!/usr/bin/python

import sys

s = sys.argv[1]

# Part 1
n = 1
# Part 2
n = int(len(s) / 2)

print(sum(
    [int(e) for i, e in enumerate(sys.argv[1]) if e == s[(i + n) % len(s)]]
))
