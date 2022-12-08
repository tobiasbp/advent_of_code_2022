#!/usr/bin/env python3

"""
Solution to https://adventofcode.com/2022/day/8
"""

from pathlib import Path

def get_visibility_map(row):
    """
    Return a list matching length of row.
    Return a list of visibility as seen from the
    left (start) of the list. 1 is visible,
    0 is invisible.
    """
    v_map = [1]

    # Run through non edge trees
    for i in range(1, len(row)-1):
        if min(max(row[:i]), max(row[i+1:])) < row[i]:
            v_map.append(1)
        else:
            v_map.append(0)
        #print(row[:i+1])

    return v_map + [1]

def get_no_of_visible_trees(data_file:Path):

    visible_trees = 0

    # Read data from data file
    data = [ l for l in data_file.read_text().split("\n") if l ]

    size = len(data[0])
    # A matrix af tree visibility.
    # 0 = invisible, 1 = visible
    v_map_rows = []
    v_map_cols = []
    v_map = size * [size * [0]]

    for row in data:
        v_map_rows.append(get_visibility_map(row))

    for col in zip(*data):
        v_map_cols.append(get_visibility_map(col))

    #v_map_colsff = list(zip(*v_map_cols))

    for row in range(size):
        for col in range(size):

            r_v = v_map_rows[row][col]
            c_v = v_map_cols[col][row]
            visible_trees += max(r_v, c_v)
            """
            print("r,c:", row, col, "rows_v:", r_v , "cols_v:", c_v, "visible:", foo := max(r_v, c_v) )
            print("foo:", foo)

            #print("r:", v_map_rows[row][col])
            #print("c:", v_map_cols[col][row])

            v_map[row][col] = foo
            print("loop:", v_map)
            """
        #print("\n")
    
    print("rows:", v_map_rows)
    print("cols:", v_map_cols)
    #print("colsT:", v_map_colsff)

    for l in data:
        print(l)
    for r in v_map:
        print(r)
    return visible_trees


assert get_no_of_visible_trees(Path("data/day_08_test.txt")) == 21

print("No of visible trees (1/2):", vt := get_no_of_visible_trees(Path("data/day_08.txt")))
assert vt == 1700
#print("Score (2/2):", s2 := calculate_rps_score(Path("data/day_02.txt"), 2))

#assert s1 == 14297
#assert s2 == 10498