#!/usr/bin/env python3

"""
Solution to https://adventofcode.com/2022/day/2
"""

from pathlib import Path

def calculate_rps_score(data_file:Path, type: int):
    """
    Calculate score from games of rock, paper scissors.
    In type 1, the data in collumn 2 dictates what I play.
    In type 2, collumn 2 dictates the needed aoutcome of the match.
    """
    score = 0

    # Read data from data file
    data = data_file.read_text()

    # Convert data to integers to alow for mathematical comparison
    for rule in [("A", 1), ("B", 2), ("C", 3), ("X", 1), ("Y", 2), ("Z", 3)]:
        data = data.replace(rule[0], str(rule[1]))

    # Raise exception if type is unexpected
    assert type in (1,2), f"Valid types are 1 & 2. Type was: {type}"
    
    # Run through the elf data.
    for line in data.split("\n"):
        # Ignore empty strings
        if line:
            # Type 1
            elfs_play, my_play = [ int(v) for v in line.split() ]
            
            # Override my_play in type2
            if type == 2:
                # 1 = elf wins, 2, = draw, 3 = I win
                result_needed = my_play

                if result_needed == 2:
                    # Draw
                    my_play = elfs_play

                elif result_needed == 3:
                    # I must win
                    if elfs_play == 3:
                        my_play = 1
                    else:
                        my_play = elfs_play + 1
                else:
                    # Elf must wins
                    if elfs_play == 1:
                        my_play = 3
                    else:
                        my_play = elfs_play - 1


            # Add score for my play
            score += my_play

            # Add score for result of match
            if elfs_play == my_play:
                # Draw
                score += 3
            elif (my_play - 1) == elfs_play:
                # I won
                score += 6            
            elif my_play == 1 and elfs_play == 3:
                # I won
                score += 6
            else:
                # I lost
                score += 0
        
    return score



print("Score (1/2):", s1 := calculate_rps_score(Path("data/day_02.txt"), 1))
print("Score (2/2):", s2 := calculate_rps_score(Path("data/day_02.txt"), 2))

assert s1 == 14297
assert s2 == 10498