#!/usr/bin/env python3

"""
Solution to https://adventofcode.com/2022/day/1
"""

from pathlib import Path

def get_calories_list(data_file:Path):
    """
    Convert a file of calories carried by elves to
    a list of the sum of calories carried by each elf.
    The data for each elf is separated by an empty line.
    """

    # Read data from data file
    data = data_file.read_text()

    # Store the calories here
    calories = []

    # Run through the elf data.
    for calories_for_elf in data.split("\n\n"):
        # Calculate the sum of calories for an elf
        calories.append(sum([ int(c) for c in calories_for_elf.split()]))
    
    return calories

c = get_calories_list(Path("data/day_01.txt"))

print("Max calories carried:", max(c))
print("Elf carying the most calories:", c.index(max(c)))
print("Sum of calories carried by the three elfs with most calories:", sum(sorted(c)[-3:]))
