"""
test_union_find.py

This module provides functionality for [brief description of what the module does].

Author: Alex Huang
Date: 2024-02-26

Classes:
    None

Functions:
    test_add_node: Tests the add_node method of the UnionFind class.
    test_union: Tests the union method of the UnionFind class.
    test_find: Tests the find method of the UnionFind class.
    test_str: Tests the __str__ method of the UnionFind class.

Notes:
    Tests basic union find operations.

Usage:
    None
"""

import pytest
import datastructures as ds

def test_add_node():
    uf = ds.UnionFind()
    uf.add_node(1)
    uf.add_node(2)
    uf.add_node(3)

    # Test adding duplicate node
    with pytest.raises(Exception):
        uf.add_node(1)

def test_union():
    uf = ds.UnionFind()
    uf.add_node(1)
    uf.add_node(2)
    uf.add_node(3)

    uf.union(1, 2)
    uf.union(2, 3)

    # Test union of nodes with same root
    assert uf.find(1) == uf.find(3)

def test_find():
    uf = ds.UnionFind()
    uf.add_node(1)
    uf.add_node(2)
    uf.add_node(3)

    uf.union(1, 2)
    uf.union(2, 3)

    assert uf.find(1) == 1
    assert uf.find(2) == 1
    assert uf.find(3) == 1

    # Test finding non-existing node
    with pytest.raises(Exception):
        uf.find(4)

# Optional: Test __str__ method
def test_str():
    uf = ds.UnionFind()
    uf.add_node(1)
    uf.add_node(2)
    uf.add_node(3)

    uf.union(1, 2)
    uf.union(2, 3)

    expected_output = "Union Find\n-----------\nObject Mapping:      [1, 2, 3]\nIndex Mapping:       [0, 0, 0]\nLength:              3"
    assert str(uf) == expected_output


