#!/usr/bin/env python3

"""
Solution to https://adventofcode.com/2022/day/4
"""

from pathlib import Path
from string import ascii_lowercase, ascii_uppercase


def no_of_overlaps(data_file:Path, contains:bool = False):
    """
    Returns number of overlapping ranges. If contains is True,
    one range must be contained in the other to be counted.
    """

    # Read data from data file (skip last empty line)
    data = data_file.read_text().split("\n")[:-1]

    no_of_overlaps = 0

    for line in data:
        # Assigments as sets consisting of all sections as integers
        a1, a2 = [ set(range(int(a.split("-")[0]), int(a.split("-")[-1])+1 )) for a in line.split(",")]
        if contains:
            # If the one set is the subset of the other
            if a1.issubset(a2) or a2.issubset(a1):
                no_of_overlaps += 1
        else:
            if not a1.isdisjoint(a2):
                no_of_overlaps += 1
    

    return no_of_overlaps

print("No of fully contained assignments:", o1 := no_of_overlaps(Path("data/day_04.txt"), True))
print("No of overlapping assignments:", o2 := no_of_overlaps(Path("data/day_04.txt"), False))

assert o1 == 496
assert o2 == 847