"""
Exercise 02: List Comprehensions
Practice: building lists in one line using comprehensions
"""

numbers = list(range(1, 11))
print("Numbers:", numbers)

# Squares of all numbers
squares = [n ** 2 for n in numbers]
print("Squares:", squares)

# Only even numbers
evens = [n for n in numbers if n % 2 == 0]
print("Evens:", evens)

# Squares of only odd numbers
odd_squares = [n ** 2 for n in numbers if n % 2 != 0]
print("Odd squares:", odd_squares)

# Convert a list of words to their lengths
words = ["python", "ml", "internship", "code"]
lengths = [len(w) for w in words]
print("Word lengths:", lengths)
