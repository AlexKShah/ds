"""
Class MyStack is an implementation of a stack data structure
Modified for proj3 to implement a priority queue and as Huffman node

__author__ = Alex Shah
__version__ = proj3
"""


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None

    def __lt__(self, other):
        if self.freq == other.freq:
            if self.is_leaf() and other.is_leaf():
                return self.char < other.char
            return self.is_leaf()
        return self.freq < other.freq


class MyPriorityQueue:
    def __init__(self):
        self.elements = []

    def push(self, item):
        # Insert item in sorted order
        index = 0
        for index, current_item in enumerate(self.elements):
            if item < current_item:
                break
        else:
            index += 1
        self.elements.insert(index, item)

    def pop(self):
        # Pop the item with the highest priority (lowest frequency)
        return self.elements.pop(0) if self.elements else None

    def __len__(self):
        return len(self.elements)

class MyStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None  # Stack is empty

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
