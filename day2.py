#!/usr/bin/python

import pandas as pd
import itertools

df = pd.read_csv('day2.csv', header=None)

# Part 1
print(sum(df.apply(lambda row: row.max() - row.min(), axis=1)))

# Part 2
print(sum(df.apply(lambda row: [int(a / b) for (a, b) in list(
        itertools.combinations(row.sort_values(ascending=False), 2)
    ) if a % b == 0][0], axis=1)))
