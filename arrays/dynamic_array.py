"""
Module Name: dynamic_array.py

This module provides a dynamic array implementation.

Author: Alex Huang
Date: 2024-02-26

Classes:
    DynamicArray: A dynamic array implementation based on the AbstractArray class.

Functions:
    None

Notes:
    This implementation supports dynamic resizing of the array to accommodate varying numbers of elements.

Usage:
    # Create a new dynamic array
    arr = DynamicArray()

    # Append elements to the array
    arr.append(1)
    arr.append(2)
    arr.append(3)

    # Pop an element from the array
    popped_element = arr.pop()

    # Insert an element at a specific index
    arr.insert(0, 4)

    # Count occurrences of an element in the array
    count = arr.count(2)

    # Remove the first occurrence of an element from the array
    arr.remove(3)

    # Extend the array with another dynamic array
    arr.extend(other_dynamic_array)

    # Create a shallow copy of the array
    arr_copy = arr.copy()
"""

from .abc_array import AbstractArray

class DynamicArray(AbstractArray):
    def __init__(self, new_list: list=[]) -> None:
        super().__init__()
        if new_list:
            self.array = new_list

    def append(self, obj, /) -> None:
        self.array.append(obj)
    
    def pop(self, index: int=-1, /) -> object:
        if len(self.array) == 0:
            raise IndexError("No elements in List to pop.")
        return self.array.pop(index)

    def insert(self, index, object, /) -> None:
        self.array.insert(index, object)
    
    def count(self, obj, /) -> int:
        count = 0
        for i in range(len(self.array)):
            if self.array[i] == obj:
                count += 1
        return count
    
    def remove(self, obj, /) -> None:
        for i in range(len(self.array)):
            if self.array[i] == obj:
                self.array.pop(i)
                return
        
        raise ValueError(f"Object to remove not found.")

    def extend(self, list: 'DynamicArray') -> None:
        self.array = self.array + list.array

    def copy(self) -> 'DynamicArray':
        copy_list = DynamicArray()
        copy_list.array = self.array.copy()
        return copy_list