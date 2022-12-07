#!/usr/bin/env python3

"""
Solution to https://adventofcode.com/2022/day/7
"""

from pathlib import Path
from math import inf

class FileSystem:
    def __init__(self):
        self.root = Directory("")
        self.cwd = self.root

class Directory:

    def __init__(self, name:str, parent=None):
        self.name = name
        self.content = []
        self.parent = parent

    def add(self, object):
        assert object.name not in [ o.name for o in self.content ], f"Object with name {object.name} already in dir {self.name}"
        assert isinstance(object.size, int)
        object.parent = self
        self.content.append(object)

    def get_by_name(self, name):

        if name == "..":
            return self.parent

        for o in self.content:
            if o.name == name:
                return o

        return None
    @property
    def path(self):
        if self.parent is None:
            return "/"
        else:
            return self.parent.name + "/" + self.name

    @property
    def size(self):
        assert isinstance(self.content, list)
        #print(self.content)
        return sum([ o.size for o in self.content ])

    def __str__(self):
        return f"dir: {self.name}"

class File:

    def __init__(self, name:str, size:int):
        self.name = name
        self.size = int(size)
    
    def __str__(self):
        return f"file: {self.name} {self.size}"

def get_file_system(data_file:Path):
    """
    Pass data and return a dict of file system
    """

    data = data_file.read_text().split("\n")

    # We always start at the root of the fs
    assert data[0] == "$ cd /"

    # All the dirs in the filesystem
    dirs = []

    # Current working directory
    root = Directory("root")
    cwd = root
    #fs = FileSystem()

    for line in data[1:-1]:
        c = line.split()

        if c[0] == "$":
            if c[1] == "cd":
                cwd = cwd.get_by_name(c[2])
                print(f"Changed dir to '{cwd.path}' with command '{line}'")
            else:
                #print("Ignoring command:", line)
                continue

        elif c[0].isdigit():
            cwd.add(File(name=c[1], size= c[0]))
        elif c[0] == "dir":
            d = Directory(name=c[1])
            cwd.add(d)
            dirs.append(d)
        else:
            raise ValueError("Could not parse line:", line)

    return root, dirs

def get_sum_of_dirs(dirs, limit:int):
    """
    Get the sum of dirs no larger than argument limit
    """
    return sum([ d.size for d in dirs if d.size <= limit ])

# Test parser with example data
root_test, dirs_test = get_file_system(Path("data/day_07_test.txt"))
assert root_test.size == 48381165
assert root_test.get_by_name("a").size == 94853
assert root_test.get_by_name("d").size == 24933642
assert root_test.get_by_name("a").get_by_name("e").size == 584
assert len(dirs_test) == 3
assert get_sum_of_dirs(dirs_test, 100000) == 95437

# The actual solutions
root, dirs = get_file_system(Path("data/day_07.txt"))
print("Size of fs:", root.size)
print("Free space on disk:", free_space := (70000000 - root.size))
print("No of dirs in fs:", len(dirs))
print("Sum of dirs below 100000 bytes:", sum_of_dirs := get_sum_of_dirs(dirs, 100000))
assert sum_of_dirs == 1432936

needed_space = 30000000
# Sorted list of all dirs big enough to get us the needed size of deleted
dirs_by_size = sorted([ d.size for d in dirs if (d.size + free_space) >= needed_space ])
print("Size of smallest dir to delete:", dirs_by_size[0])
