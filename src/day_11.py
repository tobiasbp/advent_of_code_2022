#!/usr/bin/env python3

"""
Solution to https://adventofcode.com/2022/day/11
"""

from pathlib import Path
import operator
from math import prod

ops = {
    "+": operator.add,
    "*": operator.mul
}

class Monkey:

    def __init__(self):
        self.inventory = []
        self.divisible_by = None
        self.test_true_dest = None
        self.test_false_dest = None
        self.no_of_items_inspected = 0

    def operation(self, item_value):
        if self.v2 == "old":
            v2 = item_value
        else:
            v2 = int(self.v2)

        return self.operator(item_value, v2)
     
    def throw(self):
        """
        Return value and recipient
        """
        if len(self.inventory) == 0:
            return None, None

        item_value = self.inventory.pop(0)
        #print("Orig val:", item_value)
        item_value = self.operation(item_value)
        #print("val after operation:", item_value)
        item_value = item_value // 3
        self.no_of_items_inspected += 1
        #print("val // 3:", item_value)
        if item_value % self.divisible_by == 0:
            return self.test_true_dest, item_value
        else:
            return self.test_false_dest, item_value 
    
    def recieve(self, item_value):
        self.inventory.append(item_value)

def setup_monkeys(data_file:Path):
    """
    """
    # Read data from data file
    data = [ l for l in data_file.read_text().split("\n") if l ]

    monkeys = []

    for line in data:
        if line[:6] == "Monkey":
            monkeys.append(Monkey())
        # Add items to monkey
        if "Starting items" in line:
            monkeys[-1].inventory =  [ int(item) for item in line[18:].replace(" ", "").split(",") ]
        # divide by
        if "Test: divisible by" in line:
            monkeys[-1].divisible_by = int(line.split()[-1])
        if "If true:" in line:
            monkeys[-1].test_true_dest = int(line.split()[-1])
        if "If false:" in line:
            monkeys[-1].test_false_dest = int(line.split()[-1])
        if "Operation:" in line:
            v1, op, v2 = line.split()[-3:]
            assert v1 == "old"
            monkeys[-1].operator = ops[op]
            monkeys[-1].v2 = v2


    #print("refcount:", getrefcount(v2))
    return monkeys

def play(monkeys, rounds):

    for r in range(rounds):
        for m in monkeys:
            #print("Inventory:", m.inventory)
            #print("Divisible by:", m.divisible_by)
            #print("Test True:", m.test_true_dest)
            #print("Test False:", m.test_false_dest)
            #print("Operation:", m.operation)
            #for i in range(len(m.inventory)):
            while len(m.inventory) > 0:
                recepient, item_value = m.throw()
                if recepient is None:
                    continue
                else:
                    monkeys[recepient].inventory.append(item_value)
                #print(m[recepient])
                #print("Throw:", m.throw())
            #print("---")
    
    #for i, m in enumerate(monkeys):
    #    print(f"Monkey {i}: {m.no_of_items_inspected}")
    
    return prod(sorted([ m.no_of_items_inspected for m in monkeys ])[-2:])
    

m = setup_monkeys(Path("data/day_11_test.txt"))
assert len(m) == 4
assert m[0].inventory == [79, 98]
assert m[1].inventory == [54, 65, 75, 74]
assert m[2].inventory == [79, 60, 97]
assert m[3].inventory == [74]

assert m[0].divisible_by == 23
assert m[1].divisible_by == 19
assert m[2].divisible_by == 13
assert m[3].divisible_by == 17

assert m[0].operation(10) == 190
assert m[1].operation(10) == 16
assert m[2].operation(10) == 100
assert m[3].operation(10) == 13

print("Monkey business (test):", mb := play(m, 20))
assert mb == 10605

m = setup_monkeys(Path("data/day_11.txt"))
print("Monkey business (test):", mb := play(m, 20))
assert mb == 66124
