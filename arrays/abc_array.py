"""
Module Name: abc_array.py

This module provides an abstract base class for array-like data structures.

Author: Alex Huang
Date: 2024-02-26

Classes:
    AbstractArray: An abstract base class representing array-like data structures.

Functions:
    None

Notes:
    The AbstractArray class defines abstract methods for appending elements, popping elements,
    counting occurrences of elements, and copying the array. It also implements various comparison
    and arithmetic operations, as well as iteration and containment checks.

Usage:
    # Create a subclass of AbstractArray
    class MyArray(AbstractArray):
        def append(self, value):
            pass

        def pop(self):
            pass

        def count(self, value):
            pass

        def copy(self):
            pass

    # Instantiate and use MyArray
    my_array = MyArray()
    my_array.append(5)
    my_array.append(3)
    popped_element = my_array.pop()
    count = my_array.count(5)
    copied_array = my_array.copy()
"""


from abc import ABC, abstractmethod

class AbstractArray(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.__array = []

    @property
    def array(self) -> list[object]:
        return self.__array

    @array.setter
    def array(self, new_list: list) -> None:
        if isinstance(new_list, list):
            self.__array = new_list
        else:
            raise Exception("Invalid type. Expected 'list' type.")

    @abstractmethod
    def append(self, __value) -> None:
        pass

    @abstractmethod
    def pop(self) -> object:
        pass

    @abstractmethod
    def count(self, __value) -> int:
        pass

    @abstractmethod
    def copy(self) -> 'AbstractArray':
        pass

    def __iter__(self):
        return iter(self.__array)

    def __len__(self) -> int:
        return len(self.array)
    
    def __eq__(self, __value: 'AbstractArray') -> bool:
        if len(self) != len(__value):
            return False
        
        for i in range(len(self)):
            if self.__array[i] != __value.__array[i]:
                return False
        
        return True
    
    def __ge__(self, other: 'AbstractArray') -> bool:
        for i in range(max(len(self), len(other))):
            # (self is shorter) => (self < other)
            if i == len(self):
                return False
            
            # (other is shorter) => (self > other)
            if i == len(other):
                return True
            
            # (self[i] > other[i]) => (self > other)
            if self[i] > other[i]:
                return True
            # (self[i] < other[i]) => (self < other)
            elif self[i] < other[i]:
                return False
            # (self[i] == other[i]) => (unsure)
            
        # Both List are equal
        return True
    
    def __gt__(self, other: 'AbstractArray') -> bool:
        for i in range(max(len(self), len(other))):
            # (self is shorter) => (self < other)
            if i == len(self):
                return False
            
            # (other is shorter) => (self > other)
            if i == len(other):
                return True
            
            # (self[i] > other[i]) => (self > other)
            if self[i] > other[i]:
                return True
            # (self[i] < other[i]) => (self < other)
            elif self[i] < other[i]:
                return False
            # (self[i] == other[i]) => (unsure)
            
        # Both List are equal
        return False

    def __le__(self, other: 'AbstractArray') -> bool:
        for i in range(max(len(self), len(other))):
            # (self is shorter) => (self < other)
            if i == len(self):
                return True
            
            # (other is shorter) => (self > other)
            if i == len(other):
                return False
            
            # (self[i] > other[i]) => (self > other)
            if self[i] > other[i]:
                return False
            # (self[i] < other[i]) => (self < other)
            elif self[i] < other[i]:
                return True
            # (self[i] == other[i]) => (unsure)
            
        # Both List are equal
        return True

    def __lt__(self, other: 'AbstractArray') -> bool:
        for i in range(max(len(self), len(other))):
            # (self is shorter) => (self < other)
            if i == len(self):
                return True
            
            # (other is shorter) => (self > other)
            if i == len(other):
                return False
            
            # (self[i] > other[i]) => (self > other)
            if self[i] > other[i]:
                return False
            # (self[i] < other[i]) => (self < other)
            elif self[i] < other[i]:
                return True
            # (self[i] == other[i]) => (unsure)
            
        # Both List are equal
        return False
    
    def __contains__(self, obj, /) -> bool:
        if len(self) == 0: return False

        for item in self.__array:
            if item == obj:
                return True
        
        return False

    def __add__(self, other: 'AbstractArray') -> 'AbstractArray':
        added_list = self.copy()
        for i in range(len(other)):
            added_list.append(other[i])
        return added_list

    def __iadd__(self, other: 'AbstractArray') -> None:
        self.__array += other.__array
        return self
    
    def __getitem__(self, key) -> object:
        return self.__array[key]

    def __setitem__(self, key, value) -> None:
        self.__array[key] = value
        return

    def __str__(self) -> str:
        output = "["
        for i in range(len(self)):
            output += str(self.__array[i])
            if i != len(self)-1:
                output += ", "
        output += "]"
        return output
    
    def __repr__(self) -> str:
        return str(self)
    