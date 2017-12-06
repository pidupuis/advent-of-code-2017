#!/usr/bin/python

with open("day4.txt") as f:
    s = f.read()

# Part 1
print(
    len([1 for l in [
        r for r in s.split("\n") if r
    ] if len(l.split(" ")) == len(set(l.split(" ")))])
)

# Part 2
i = 0
for l in [r for r in s.split("\n") if r]:
    words = [''.join(sorted(w)) for w in l.split(" ")]
    if len(words) == len(set(words)):
        i += 1
print(i)
