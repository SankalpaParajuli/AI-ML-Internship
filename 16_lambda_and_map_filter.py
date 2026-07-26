"""
Exercise 16: Lambda, map(), and filter()
Practice: functional-style Python, useful later for data manipulation
"""

numbers = list(range(1, 11))

# lambda + map: square every number
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)

# lambda + filter: keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)

# lambda + sorted: sort strings by length
words = ["python", "ml", "internship", "ai", "data"]
sorted_by_length = sorted(words, key=lambda w: len(w))
print("Sorted by length:", sorted_by_length)

# combining map + filter: squares of even numbers only
even_squares = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print("Squares of evens:", even_squares)
