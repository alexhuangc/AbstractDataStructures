"""
Module Name: queue.py

This module provides an implementation of a queue data structure.

Author: Alex Huang
Date: 2024-02-26

Classes:
    Queue: A class representing a queue data structure.

Functions:
    None

Notes:
    The Queue class provides methods for appending elements, popping elements, peeking at the front element,
    counting occurrences of elements, checking if the queue is empty, and copying the queue.

Usage:
    # Create a new Queue instance
    q = Queue()

    # Append elements to the queue
    q.append(5)
    q.append(3)
    q.append(7)

    # Pop an element from the queue
    popped_element = q.pop()

    # Peek at the front element of the queue
    front_element = q.peek()

    # Count occurrences of an element
    count = q.count(5)

    # Check if the queue is empty
    is_empty = q.is_empty()

    # Create a copy of the queue
    copied_queue = q.copy()
"""

from .abc_array import AbstractArray

class Queue(AbstractArray):
    def __init__(self) -> None:
        super().__init__()
        self.__head_index = 0
        self.__tail_index = 0
        self.__is_empty = True
        self.__array_size = 0
    
    def append(self, __value, /):
        # fast implementation and wrapping
        pass
        

    def pop(self) -> object:
        # fast implementation and wrapping
        pass

    def peek(self) -> object:
        return self.array[self.__head_index]

    def count(self, __value) -> int:
        count = 0
        for i in range(len(self)):
            if self.array[i] == __value:
                count += 1
        return count

    def is_empty(self) -> bool:
        return self.__is_empty

    def copy(self) -> 'Queue':
        copy_queue = Queue()
        copy_queue.__array = self.array.copy()
        copy_queue.__head_index = self.__head_index
        copy_queue.__tail_index = self.__tail_index
        return copy_queue

    def __at_capacity(self) -> bool:
        # return len(self) =
        pass
        


if __name__ == '__main__':
    q = Queue()
    