"""
Module Name: datastructures/__init__.py
"""

import sys
import os

# Get the directory containing the __init__.py file (i.e., the package directory)
package_dir = os.path.abspath(os.path.dirname(__file__))

# Add the parent directory of the package directory to the Python path
parent_dir = os.path.dirname(package_dir)
sys.path.append(parent_dir)

from .arrays import (
    DynamicArray,
    HeapQueue,
    Queue,
    Stack,
)

from .graphs import (
    UnionFind,
)

# from .trees import (

# )

__all__ = [
    'DynamicArray',
    'HeapQueue',
    'Queue',
    'Stack',
    'UnionFind',
]
