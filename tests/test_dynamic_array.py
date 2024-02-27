"""
test_dynamic_array.py

This module provides functionality for [brief description of what the module does].

Author: Alex Huang
Date: 2024-02-26

Classes:
    None

Functions:
    test_append
    test_pop
    test_count
    test_insert
    test_remove
    test_extend
    test_copy

Notes:
    Tests basic dynamic array operations.

Usage:
    None
"""

import pytest
import datastructures as ds

def test_append():
    # Create an instance of List
    arr = ds.DynamicArray()

    # Append some elements
    arr.append(1)
    arr.append(2)
    arr.append(3)

    # Check if elements are appended correctly
    assert len(arr) == 3
    assert arr[0] == 1
    assert arr[1] == 2
    assert arr[2] == 3

    # Append more elements
    arr.append(4)
    arr.append(5)

    # Check if size is increased and elements are appended correctly
    assert len(arr) == 5
    assert arr[3] == 4
    assert arr[4] == 5

def test_pop():
    arr = ds.DynamicArray([1, 2, 3, 4, 5])

    # Test pop without index
    assert arr.pop() == 5
    assert len(arr) == 4

    # Test pop with index
    assert arr.pop(1) == 2
    assert len(arr) == 3
    assert arr[1] == 3

    # Test pop on empty array
    arr = ds.DynamicArray()
    with pytest.raises(IndexError):
        arr.pop()

def test_count():
    arr = ds.DynamicArray([1, 2, 2, 3, 3, 3])

    # Test count
    assert arr.count(2) == 2
    assert arr.count(3) == 3
    assert arr.count(4) == 0

def test_insert():
    arr = ds.DynamicArray([1, 2, 3])

    # Test insert
    arr.insert(1, 5)
    assert len(arr) == 4
    assert arr[1] == 5
    assert arr[2] == 2

    # Test insert at end
    arr.insert(4, 6)
    assert len(arr) == 5
    assert arr[4] == 6

def test_remove():
    arr = ds.DynamicArray([1, 2, 3, 4, 5])

    # Test remove
    arr.remove(3)
    assert len(arr) == 4
    assert arr[2] == 4

    # Test remove non-existing element
    with pytest.raises(ValueError):
        arr.remove(6)

def test_extend():
    arr1 = ds.DynamicArray([1, 2, 3])
    arr2 = ds.DynamicArray([4, 5, 6])

    # Test extend
    arr1.extend(arr2)
    assert len(arr1) == 6
    assert arr1[3] == 4

def test_copy():
    arr = ds.DynamicArray([1, 2, 3])

    # Test copy
    arr_copy = arr.copy()
    assert arr_copy == arr
    assert arr_copy is not arr  # Ensure different objects