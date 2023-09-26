"""
Class MyStack is an implementation of a stack data structure

__author__ = Alex Shah
"""


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
