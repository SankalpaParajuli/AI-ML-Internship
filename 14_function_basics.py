"""
Exercise 14: Function Basics
Practice: default args, *args, **kwargs, return values
"""


def greet(name, greeting="Hello"):
    """Function with a default argument."""
    return f"{greeting}, {name}!"


def add_all(*numbers):
    """Function using *args to accept any number of positional arguments."""
    return sum(numbers)


def print_profile(**details):
    """Function using **kwargs to accept any number of keyword arguments."""
    for key, value in details.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    print(greet("Sankalpa"))
    print(greet("Anurag", greeting="Namaste"))

    print("\nSum of 1,2,3:", add_all(1, 2, 3))
    print("Sum of 5,10,15,20:", add_all(5, 10, 15, 20))

    print("\nProfile:")
    print_profile(name="Sankalpa", role="AI/ML Intern", company="Code-IT")
