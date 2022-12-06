#!/usr/bin/env python3

"""
Solution to https://adventofcode.com/2022/day/6
"""

from pathlib import Path

def get_packet_pos(data_file:Path, packet_length: int):
    """
    Return index of last character position in first occurrence of
    a substring of length_packet_length with all unique characters.
    """

    data = data_file.read_text()

    for i in range(len(data)-packet_length):
        f = set(data[i:i+packet_length])
        if len(f) == packet_length:
            return i + packet_length


print("Start of packet pos:", sop := get_packet_pos(Path("data/day_06.txt"), 4))
print("Start of message pos:", som := get_packet_pos(Path("data/day_06.txt"), 14))

assert sop == 1356
assert som == 2564
