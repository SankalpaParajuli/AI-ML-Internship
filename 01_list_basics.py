"""
Exercise 01: List Basics
Practice: creating lists, indexing, slicing, append, insert, remove
"""

fruits = ["apple", "banana", "cherry", "mango"]
print("Original list:", fruits)

# Indexing and slicing
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("First two fruits:", fruits[:2])

# Adding items
fruits.append("orange")
fruits.insert(1, "kiwi")
print("After append + insert:", fruits)

# Removing items
fruits.remove("banana")
popped = fruits.pop()
print("After remove + pop:", fruits)
print("Popped item:", popped)

# Sorting
fruits.sort()
print("Sorted:", fruits)

fruits.sort(reverse=True)
print("Reverse sorted:", fruits)
