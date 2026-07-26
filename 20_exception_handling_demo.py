"""
Exercise 20: Exception Handling
Practice: try/except/else/finally, custom errors, input validation
"""


def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Both inputs must be numbers.")
        return None
    else:
        print("Division succeeded.")
        return result
    finally:
        print(f"Attempted to divide {a} by {b}\n")


def get_positive_number(value):
    """Raises a custom-style error if number is not positive."""
    if not isinstance(value, (int, float)):
        raise TypeError(f"{value} is not a number")
    if value <= 0:
        raise ValueError(f"{value} is not a positive number")
    return value


if __name__ == "__main__":
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
    print(safe_divide(10, "a"))

    for val in [5, -3, "hello"]:
        try:
            print("Valid positive number:", get_positive_number(val))
        except (TypeError, ValueError) as e:
            print("Caught error:", e)
