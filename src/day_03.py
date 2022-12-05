#!/usr/bin/env python3

"""
Solution to https://adventofcode.com/2022/day/3
"""

from pathlib import Path
from string import ascii_lowercase, ascii_uppercase

def get_priority(item:str):
    return (ascii_lowercase + ascii_uppercase).index(item) + 1

def get_sum_of_priorities(data_file:Path):
    """
    Get the sum of priorities of all items in
    both compartments in rucksack.
    """

    # Read data from data file
    data = data_file.read_text()
    
    sum_of_priorities = 0

    # Run through the elf data.
    for line in data.split("\n"):
        # Split line into contents of compartment 1 & 2
        c1 = line[0:len(line)//2]
        c2 = line[len(line)//2:]

        assert c1 + c2 == line
        assert len(line)%2 == 0

        # Run through items in compartment 1 looking
        # for a match in compartment 2
        for item in c1:
            if item in c2:
                sum_of_priorities += get_priority(item)

                break

    return sum_of_priorities

def get_sum_of_group_badge_priorities(data_file:Path):

    # Read data from data file
    data = data_file.read_text().split("\n")

    sum_of_priorities = 0

    for i in range(len(data)//3):
        # Create a set for items carried by each elf
        e1, e2, e3 = [set(d) for d in (data[i*3:i*3+3])]

        # Find common item across elves
        common_item = list(e1 & e2 & e3)

        assert len(common_item) == 1
        
        # Add the priority of the common item
        sum_of_priorities += get_priority(common_item[0])

    return sum_of_priorities

assert get_priority("p") == 16
assert get_priority("L") == 38
assert get_priority("P") == 42
assert get_priority("v") == 22
assert get_priority("t") == 20
assert get_priority("s") == 19


print("Sum of priorities:", s1 := get_sum_of_priorities(Path("data/day_03.txt")))
print("Sum of badge priorities:",s2 := get_sum_of_group_badge_priorities(Path("data/day_03.txt")))

assert s1 == 8243
assert s2 == 2631