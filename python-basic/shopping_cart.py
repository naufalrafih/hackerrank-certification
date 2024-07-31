#!/bin/python3

import math
import os
import random
import re
import sys


class Item:
    # Implement the Item here
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

class ShoppingCart:
    # Implement the ShoppingCart here
    def __init__(self, item=None):
        if item is None:
            self.item = []
        else:
            self.item = item

    def __len__(self):
        return len(self.item)

    def add(self, item):
        self.item.append(item)

    def total(self):
        total = 0
        for item in self.item:
            total += item.price
        return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    items = []
    for _ in range(n):
        name, price = input().split()
        item = Item(name, int(price))
        items.append(item)

    cart = ShoppingCart()

    q = int(input())
    for _ in range(q):
        line = input().split()
        command, params = line[0], line[1:]
        if command == "len":
            fptr.write(str(len(cart)) + "\n")
        elif command == "total":
            fptr.write(str(cart.total()) + "\n")
        elif command == "add":
            name = params[0]
            item = next(item for item in items if item.name == name)
            cart.add(item)
        else:
            raise ValueError("Unknown command %s" % command)

    fptr.close()
