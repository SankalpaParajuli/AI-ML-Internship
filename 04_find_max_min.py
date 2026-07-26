"""
Exercise 04: Find Max and Min
Practice: loops, comparisons, functions
"""


def find_max(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


def find_min(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest


if __name__ == "__main__":
    values = [12, 45, 2, 89, 33, 7]
    print("Numbers:", values)
    print("Max (manual):", find_max(values))
    print("Min (manual):", find_min(values))
    print("Max (built-in):", max(values))
    print("Min (built-in):", min(values))
