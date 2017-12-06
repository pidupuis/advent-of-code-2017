#!/usr/bin/python

spirale = [{
    "v": 1,
    "x": 0,
    "y": 0,
}]

p = 277678
x = y = 0
dx = 0
dy = -1
i = 2
while True:
    v = 0
    for j in spirale:
        manhattan = abs(j.get("x") - x) + abs(j.get("y") - y)
        if manhattan == 1 or (manhattan == 2 and (
            abs(j.get("x") - x) != 0 and abs(j.get("y") - y) != 0
        )):
            v += j.get("v")
    if v > p:
        print(v)
        break
    spirale.append({
        "v": v,
        "x": x,
        "y": y,
    })
    if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
        dx, dy = -dy, dx
    x, y = x+dx, y+dy
