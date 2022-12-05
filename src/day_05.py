#!/usr/bin/env python3

"""
Solution to https://adventofcode.com/2022/day/5
"""

from pathlib import Path

def move_crates(data_file:Path, crane_model: int):
    """
    Simulate the reordering of crates using one of the supported crane models
    """

    assert crane_model in [9000, 9001], f"Unupported crane model: {crane_model}"

    # Read data from data file (skip last empty line)
    data = [ line for line in data_file.read_text().split("\n") if line ]

    crates = []
    commands = []

    # Parse the data into commands and crate positions
    for line in data:
        if "move" in line.lower():
            
            # Build a dictionary for each command for clarity
            command = {}
            for key, value in zip(["no_of_crates", "source", "dest"], [ int(c) for c in line.split() if c.isdigit() ]):
                command[key] = value
            commands.append(command)
        else:
            # Extract every 4th value from the crate strings
            # as rows in the crates pamtrix
            c =  [ line[i] for i in range(1, len(line), 4) ]
            crates.append(c)


    # Transform list of crate rows into a list of crate collumns
    crates = list(zip(*crates))

    # Cleanup crate collumns
    for i in range(len(crates)):
        # Remove empty positions in crate collumns
        crates[i] = [ c for c in crates[i] if c != " " ]
        # Make sure last entry is bottom of collumn
        assert crates[i][-1].isdigit()

    for c in commands:
        # Crates to move from source
        crates_to_move = crates[c["source"]-1][:c["no_of_crates"]]
        # If the crane model is 9000, we can only move one
        # crate at a time. This means the ordering of the crates
        # will be reversed in the destination collumn
        if crane_model == 9000:
            crates_to_move = list(reversed(crates_to_move))
        # Remove crates from source
        crates[c["source"]-1] = crates[c["source"]-1][c["no_of_crates"]:]
        # Reverse crate order and insert at beginning of destination
        crates[c["dest"]-1] = crates_to_move + crates[c["dest"]-1]
    
    # Return a string characters representing the top crates in the collumns
    return "".join([ col[0] for col in crates ])

print("Cratet on top when moved with 9000:", crates_9000 := move_crates(Path("data/day_05.txt"), crane_model=9000))
print("Crates on top when moved with 9001:", crates_9001 := move_crates(Path("data/day_05.txt"), crane_model=9001))

assert crates_9000 == "ZWHVFWQWW"
assert crates_9001 == "HZFZCCWWV"
