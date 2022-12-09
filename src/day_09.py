#!/usr/bin/env python3

"""
Solution to https://adventofcode.com/2022/day/9
"""

from pathlib import Path
from math import sqrt

def get_new_pos(pos, vec):
    """
    Calculate new position from a vecor and a position
    """
    return (pos[0] + vec[0], pos[1] + vec[1])

def add_vectors(v1, v2):
    """
    Add two vectors
    """
    return (v1[0] + v2[0], v1[1] + v2[1])

def get_vector(dir: str):
    """
    Get a vector from a direction
    """
    if dir == "R":
        return (1, 0)
    elif dir == "D":
     return (0, -1)
    elif dir == "L":
        return (-1, 0)
    elif dir == "U":
        return (0, 1)
    else:
        raise ValueError("Invalid direction:", dir)

def are_adjacent(pos_a, pos_b) -> bool:
    diff_x = pos_a[0] - pos_b[0]
    diff_y = pos_a[1] - pos_b[1]
    dist = sqrt(diff_x**2 + diff_y**2)
    print(dist)
    return dist < 2.0

def get_no_of_positions(data_file:Path):
    """
    """

    # Read data from data file
    data = [ l for l in data_file.read_text().split("\n") if l ]

    p_head = (1,1)
    #p_head_prev = None
    p_tail = (1,1)

    positions_visited_by_tail = {p_tail}
    no_of_tail_moves = 0
    for command in data:
        dir, no_of_steps = command.split()
        assert no_of_steps.isdigit()

        for i in range(int(no_of_steps)):
            print("h:", p_head, "t:", p_tail)

            p_head_prev = p_head
            v_head = get_vector(dir)
            p_head = get_new_pos(p_head, v_head)

            #print("Calculate diff between (h,t):", p_head, p_tail)
            # Diff between head and potential new tail pos
            if not are_adjacent(p_head, p_tail):
                no_of_tail_moves += 1
                p_tail = p_head_prev
                positions_visited_by_tail.add(p_tail)
                print("h:", p_head, "t:", p_tail)

            """
            if abs(p_head[0] - p_tail[0]) == 1 and abs(p_head[1] - p_tail[1]) == 1:
                print("Don't move tail from", p_tail, "to", p_head_prev)
            else:
                p_tail = p_head_prev
                positions_visited_by_tail.add(p_tail)
            """

            #diff_sum = abs(p_head[0] - p_tail[0]) + abs(p_head[1] - p_tail[1])
            
            #print("Move tail to:", p_tail, f"(diff_sum: {diff_sum})")

            print("----")
            """
            print("Diff x:", abs(p_head_prev[0] - p_tail[0]), "Diff y:", abs(p_head_prev[1] - p_tail[1]))
            diff_sum = abs(p_head_prev[0] - p_tail[0]) + abs(p_head_prev[1] - p_tail[1])
            print("Diff sum:", diff_sum)
            if diff_sum != 1:
                p_tail = p_head_prev
                print("MOve tail to:", p_tail)

            #v_tail = (p_tail[0] + p_head[0], p_tail[1] + p_head[1] )
            #p_tail =
            print("----") 
            #print("h:", p_head, "t:", p_tail)

            #print(dir, i, p_head)    
            """
    print("No of tail moves:", no_of_tail_moves)
    print(positions_visited_by_tail)
    return len(positions_visited_by_tail)




assert get_no_of_positions(Path("data/day_09_test.txt")) == 13
print("No of unique positions visited by tail:", np := get_no_of_positions(Path("data/day_09.txt")))
