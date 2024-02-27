"""
Module Name: heap_queue.py

This module provides an implementation of a heap-based priority queue.

Author: Alex Huang
Date: 2024-02-26

Classes:
    HeapQueue: A class representing a heap-based priority queue.

Functions:
    None

Notes:
    The HeapQueue class provides methods for appending elements, popping elements with the highest priority,
    counting occurrences of elements, copying the priority queue, and heapifying a list into a heap.

Usage:
    # Create a new HeapQueue instance
    min_heap = HeapQueue(priority_type='min')

    # Append elements to the priority queue
    min_heap.append(5)
    min_heap.append(3)
    min_heap.append(7)

    # Pop the element with the highest priority (min heap)
    popped_element = min_heap.pop()

    # Count occurrences of an element
    count = min_heap.count(5)

    # Create a copy of the priority queue
    copied_heap = min_heap.copy()

    # Heapify a list into a heap
    heap_list = [3, 2, 1, 4, 5]
    min_heap.heapify(heap_list)
"""

from .abc_array import AbstractArray

class HeapQueue(AbstractArray):
    def __init__(self, priority_type: str='min') -> None:
        super().__init__()
        if priority_type == 'min' or priority_type == 'max':
            self.__PRIORITY_TYPE = priority_type
        else:
            raise Exception("priority_type must be either 'min' or 'max' for a min heap or max heap.")

    def append(self, __value) -> None:
        self.array.append(__value)
        self.__sift_up(len(self.array) - 1)

    def pop(self) -> object:
        
        pass

    def count(self, __value) -> int:
        pass

    def copy(self) -> 'AbstractArray':
        pass

    def heapify(self, heapify_list: list) -> None:
        pass

    def __sift_up(self, index):
        current_index = index
        # Min Heap
        if self.__PRIORITY_TYPE == 'min':
            parent_index = (current_index - 1) // 2
            while parent_index >= 0 and self.array[current_index] < self.array[parent_index]:
                # Swap child and parent
                child = self.array[current_index]
                self.array[current_index] = self.array[parent_index]
                self.array[parent_index] = child
                # reset index
                current_index = parent_index
                parent_index = (current_index - 1) // 2
        # Max Heap
        else:
            parent_index = (current_index - 1) // 2
            while parent_index >= 0 and self.array[current_index] > self.array[parent_index]:
                # Swap child and parent
                child = self.array[current_index]
                self.array[current_index] = self.array[parent_index]
                self.array[parent_index] = child
                # reset index
                current_index = parent_index
                parent_index = (current_index - 1) // 2

    