#!/usr/bin/env python3

"""
Solution to https://adventofcode.com/2022/day/7
"""

from pathlib import Path

class Directory:

    def __init__(self, name:str, parent=None):
        self.name = name
        self.content = []
        self.parent = parent

    def add(self, object):
        assert object.name not in [ o.name for o in self.content ], f"Object with name {object.name} already in dir {self.name}"
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
        return sum([ o.size for o in self.content ])

    def __str__(self):
        return f"dir: {self.name}"

class File:

    def __init__(self, name:str, size:int, parent=None):
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

    # Current working directory
    root = Directory("root")
    cwd = root

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
            cwd.add(Directory(name=c[1]))
        else:
            raise ValueError("Could not parse line:", line)
        #print(line)
        #print("cwd:", cwd, cwd.size)
        #print([ str(o) for o in cwd.content])

    return root

# Test parser with example
root_test = get_file_system(Path("data/day_07_test.txt"))
assert root_test.size == 48381165
assert root_test.get_by_name("a").size == 94853
assert root_test.get_by_name("d").size == 24933642
assert root_test.get_by_name("a").get_by_name("e").size == 584
