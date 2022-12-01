#!/usr/bin/env python3

"""
Solution to https://adventofcode.com/2022/day/1
"""

from pathlib import Path

def get_calories_list(data_file:Path):
    """
    Convert a file of calories carried by gnomes to
    a list of the sum of calories carried by each gnome.
    Each gnome is separated by an empty line.
    """

    # Read data from data file
    data = data_file.read_text()

    # Store the calories here
    calories = []

    # Run through the gnome data.
    for calories_for_gnome in data.split("\n\n"):
        # Calculate the sum of calories for a gnome
        calories.append(sum([ int(c) for c in calories_for_gnome.split()]))
    
    return calories

c = get_calories_list(Path("data/day_01.data"))

print("Max calories carried:", max(c))
print("Carried by gnome no:", c.index(max(c)))
print("Sum of calories carried by the three gnomes with most calories:", sum(sorted(c)[-3:]))
