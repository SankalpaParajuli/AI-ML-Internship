"""
Exercise 13: Prime Number Checker
Practice: loops, conditionals, functions, math basics
"""


def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


if __name__ == "__main__":
    print("Prime numbers between 1 and 50:")
    primes = [n for n in range(1, 51) if is_prime(n)]
    print(primes)
