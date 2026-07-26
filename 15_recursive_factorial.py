"""
Exercise 15: Recursive Factorial
Practice: recursion, base cases, functions
"""


def factorial_recursive(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    for num in [0, 1, 5, 7, 10]:
        print(f"{num}! (recursive) = {factorial_recursive(num)}")
        print(f"{num}! (iterative) = {factorial_iterative(num)}")
