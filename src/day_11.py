#!/usr/bin/env python3

"""
Solution to https://adventofcode.com/2022/day/11
"""

import operator
import cProfile

from pathlib import Path
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
        self.worry_divisor = None
        self.product_of_divisors = None

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
        item_value = self.operation(item_value)
        item_value = item_value // self.worry_divisor
        self.no_of_items_inspected += 1
        item_value = item_value % self.product_of_divisors
        if item_value % self.divisible_by == 0:
            return self.test_true_dest, item_value
        else:
            return self.test_false_dest, item_value 
    
    def recieve(self, item_value):
        self.inventory.append(item_value)

def setup_monkeys(data_file:Path, worry_divisor: int):
    """
    """
    # Read data from data file
    data = [ l for l in data_file.read_text().split("\n") if l ]

    monkeys = []

    for line in data:
        if line[:6] == "Monkey":
            m = Monkey()
            m.worry_divisor = worry_divisor
            monkeys.append(m)
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

    # Monkey need to now product of divisors for efficiency
    product_of_divisors = prod([ m.divisible_by for m in monkeys ])
    for m in monkeys:
        m.product_of_divisors = product_of_divisors

    return monkeys

def play(monkeys, rounds):

    for r in range(rounds):
        for m in monkeys:
            # Monkey throws all items it has
            while len(m.inventory) > 0:
                recepient, item_value = m.throw()
                #print(item_value)
                if recepient is None:
                    continue
                else:
                    monkeys[recepient].inventory.append(item_value)

    for i, no_of_items_inspected in enumerate([ m.no_of_items_inspected for m in monkeys ]):
        print(f"Monkey {i}: {no_of_items_inspected}")

    # Product of no of items trown by top two most active monkeys    
    return prod(sorted([ m.no_of_items_inspected for m in monkeys ])[-2:])
    

m = setup_monkeys(Path("data/day_11_test.txt"), 3)
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

print("Monkey business (wd=3, test):", mb_t_wd3 := play(m, 20))
assert mb_t_wd3 == 10605

m = setup_monkeys(Path("data/day_11_test.txt"), 1)
print("Monkey business (wd=1, test):", mb_t_wd1 := play(m, 10000))
assert mb_t_wd1 == 2713310158

m = setup_monkeys(Path("data/day_11.txt"), 3)
print("Monkey business (wd=3):", mb_wd3 := play(m, 20))
assert mb_wd3 == 66124

m = setup_monkeys(Path("data/day_11.txt"), 1)
print("Monkey business (wd=1):", mb_wd1 := play(m, 10000))
assert mb_wd1 == 19309892877
