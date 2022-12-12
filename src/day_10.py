#!/usr/bin/env python3

"""
Solution to https://adventofcode.com/2022/day/9
"""

from pathlib import Path
from math import sqrt


def get_values_for_x(data_file:Path, cycles_of_interest):
    """
    """
    # Read data from data file
    data = [ l for l in data_file.read_text().split("\n") if l ]

    #cycle = 0
    x = 1

    # History of the value of x.
    # Entries are for the value of x after index 
    history = []

    for line in data:
        if line == "noop":
            #cycle += 1
            history.append(x)
        elif "addx" in line:
            history.append(x)
            value = int(line.split()[-1])
            x += value
            history.append(x)
        else:
            raise ValueError("Unknown command:", line)

    #for i, v in enumerate(history):
    #    print(f"Cycle {i+1}: {v}")
    sum_of_frequencies = 0
    for c in cycles_of_interest:
        print(c, ":", history[c-2])
        sum_of_frequencies += c * history[c-2]
    return sum_of_frequencies


assert get_values_for_x(Path("data/day_10_test.txt"), [20, 60, 100, 140, 180, 220]) == 13140

assert get_values_for_x(Path("data/day_10.txt"), [20, 60, 100, 140, 180, 220]) == 17940

#assert get_no_of_positions(Path("data/day_09_test.txt"), 2) == 13
#assert get_no_of_positions(Path("data/day_09_test.txt"), 10) == 1

#print("No of unique positions visited by tail:", np := get_no_of_positions(Path("data/day_09.txt")))
