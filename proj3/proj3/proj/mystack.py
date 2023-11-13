"""
Class MyStack is an implementation of a stack data structure
Modified for proj3 to implement a priority queue and as Huffman node

__author__ = Alex Shah
__version__ = proj3
"""


class MyPriorityQueue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        # Sort by frequency, then single-letter precedence, then alphabetically
        self.items.sort(key=lambda x: (x.freq, len(x.char) if x.char else 0, x.char if x.char else ""))

    def pop(self):
        return self.items.pop(0) if self.items else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


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
