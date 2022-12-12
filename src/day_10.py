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

    x = 1

    # History of the value of x.
    # Value is value of x during cycle no (starting at 0) 
    history = [x]

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

    # Render screen as one long line
    screen = ""
    for cycle_no, x in enumerate(history):
        line_pos = cycle_no%40
        if line_pos in [ x-1, x , x+1 ]:
            screen += "#"
        else:
            screen += "."

    # Display screen as lines of 40 characters
    for line_no in range(6):
        print(screen[line_no*40: line_no*40 + 40])
 
    sum_of_frequencies = 0
    for c in cycles_of_interest:
        # input frequencies has 1 as first cycle, but we have 0, so adjust by -1
        sum_of_frequencies += c * history[c-1]
    return sum_of_frequencies


assert get_values_for_x(Path("data/day_10_test.txt"), [20, 60, 100, 140, 180, 220]) == 13140
print()
assert get_values_for_x(Path("data/day_10.txt"), [20, 60, 100, 140, 180, 220]) == 17940

