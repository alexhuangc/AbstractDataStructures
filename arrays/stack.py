"""
Module Name: stack.py

This module provides an implementation of a stack data structure.

Author: Alex Huang
Date: 2024-02-26

Classes:
    Stack: A class representing a stack data structure.

Functions:
    None

Notes:
    The Stack class provides methods for appending elements, popping elements, counting occurrences of elements,
    and copying the stack.

Usage:
    # Create a new Stack instance
    stack = Stack()

    # Append elements to the stack
    stack.append(5)
    stack.append(3)
    stack.append(7)

    # Pop an element from the stack
    popped_element = stack.pop()

    # Count occurrences of an element
    count = stack.count(5)

    # Create a copy of the stack
    copied_stack = stack.copy()
"""


from .abc_array import AbstractArray

class Stack(AbstractArray):
    def __init__(self) -> None:
        super().__init__()

    def append(self, __value) -> None:
        self.array.append(__value)
    
    def pop(self) -> object:
        if len(self) > 0:
            self.array.pop(-1)
        else:
            raise Exception("Cannot pop from empty stack.")
    
    def count(self, __value) -> int:
        count = 0
        for i in range(len(self)):
            if self.array[i] == __value:
                count += 1
        return count

    def copy(self) -> 'Stack':
        copy_stack = Stack()
        copy_stack.__array = self.array.copy()
        return copy_stack