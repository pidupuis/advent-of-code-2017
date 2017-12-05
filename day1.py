#!/usr/bin/python

with open("day1.txt") as f:
    s = f.read().strip()

# Part 1
n = 1
# Part 2
n = int(len(s) / 2)

print(sum(
    [int(e) for i, e in enumerate(s) if e == s[(i + n) % len(s)]]
))
