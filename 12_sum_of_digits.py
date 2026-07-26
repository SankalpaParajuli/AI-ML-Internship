"""
Exercise 12: Sum of Digits
Practice: loops, modulo, integer division, functions
"""


def sum_of_digits(number):
    number = abs(number)
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total


if __name__ == "__main__":
    for n in [12345, 987, 100, -456]:
        print(f"Sum of digits in {n} = {sum_of_digits(n)}")
