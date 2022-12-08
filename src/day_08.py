#!/usr/bin/env python3

"""
Solution to https://adventofcode.com/2022/day/8
"""

from pathlib import Path

def get_visibility_map(row):
    """
    Return a list of visibility as seen from the
    either end of the row. 1 is visible, 0 is invisible.
    """
    v_map = [1]

    # Run through non edge trees
    for i in range(1, len(row)-1):
        if min(max(row[:i]), max(row[i+1:])) < row[i]:
            v_map.append(1)
        else:
            v_map.append(0)

    return v_map + [1]

def get_viewing_distance(row):
    """
    Return a list of visibility for the trees in row.
    Trees on edge has a score of 0.
    """
    dist_map = [0]

    # Run through non edge trees
    for i in range(1, len(row)-1):
        l = row[:i]
        r = row[i+1:]

        # Number of visible trees to the left
        v_l = 0
        for h in reversed(l):
            v_l += 1
            if h >= row[i]:
                break

        # Number of visible trees to the right
        v_r = 0
        for h in r:
            v_r += 1
            if h >= row[i]:
                break

        # The visibility score for current tree
        dist_map.append(v_l * v_r)

    return dist_map + [0]

def evaluate_forest(data_file:Path):
    """
    Return number of visible trees in forest
    Return best viewing distance
    """

    visible_trees = 0
    best_viewing_distance = 0

    # Read data from data file
    data = [ l for l in data_file.read_text().split("\n") if l ]

    size = len(data[0])

    # Tree visibility
    # 0 = invisible, 1 = visible
    v_map_rows = []
    v_map_cols = []

    d_map_rows = []
    d_map_cols = []

    # Evaluate rows
    for row in data:
        v_map_rows.append(get_visibility_map(row))
        d_map_rows.append(get_viewing_distance(row))

    # Evaluate collumns
    for col in zip(*data):
        v_map_cols.append(get_visibility_map(col))
        d_map_cols.append(get_viewing_distance(col))

    for row in range(size):
        for col in range(size):

            visible_trees += max(v_map_rows[row][col], v_map_cols[col][row])
            best_viewing_distance = max( best_viewing_distance, d_map_rows[row][col] * d_map_cols[col][row])

    return visible_trees, best_viewing_distance

t_trees, t_dist = evaluate_forest(Path("data/day_08_test.txt"))
assert t_trees == 21
assert t_dist == 8

trees, dist = evaluate_forest(Path("data/day_08.txt"))
print("No of visible trees:", trees)
print("Best distance:", dist)

assert trees == 1700
assert dist == 470596