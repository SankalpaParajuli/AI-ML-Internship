"""
Week 2 - NumPy Exercises
AI/ML Internship - Code-IT
Author: Sankalpa Parajuli

Covers: array creation, indexing/slicing, broadcasting, and
vectorized operations, as required by the Week 2 task list.
"""

import numpy as np


def array_creation():
    print("--- Array Creation ---")
    zeros = np.zeros((2, 3))
    ones = np.ones((3, 2))
    ranged = np.arange(0, 10, 2)
    linspace = np.linspace(0, 1, 5)
    identity = np.eye(3)

    print("Zeros:\n", zeros)
    print("Ones:\n", ones)
    print("Arange (0-10, step 2):", ranged)
    print("Linspace (0-1, 5 points):", linspace)
    print("Identity matrix:\n", identity)


def indexing_and_slicing():
    print("\n--- Indexing & Slicing ---")
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Original array:\n", arr)
    print("Element at row 1, col 2:", arr[1, 2])
    print("First row:", arr[0, :])
    print("Last column:", arr[:, -1])
    print("Sub-matrix (rows 0-1, cols 1-2):\n", arr[0:2, 1:3])
    print("Values greater than 5:", arr[arr > 5])


def broadcasting():
    print("\n--- Broadcasting ---")
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([10, 20, 30])
    print("Array a:\n", a)
    print("Array b:", b)
    print("a + b (broadcast over rows):\n", a + b)

    c = np.array([[1], [2]])
    print("Array c:\n", c)
    print("a + c (broadcast over columns):\n", a + c)


def vectorized_operations():
    print("\n--- Vectorized Operations ---")
    arr = np.array([1, 2, 3, 4, 5])
    print("Array:", arr)
    print("Squared:", arr ** 2)
    print("Square root:", np.sqrt(arr))
    print("Sum:", arr.sum())
    print("Mean:", arr.mean())
    print("Standard deviation:", arr.std())

    # Vectorized vs loop comparison (concept check)
    squared_loop = [x ** 2 for x in arr]
    print("Loop-based squared (for comparison):", squared_loop)


if __name__ == "__main__":
    array_creation()
    indexing_and_slicing()
    broadcasting()
    vectorized_operations()
