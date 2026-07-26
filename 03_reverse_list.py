"""
Exercise 03: Reverse a List
Practice: writing a function, loops, and using built-ins
"""


def reverse_list_manual(items):
    """Reverse a list without using built-in reverse() or slicing."""
    reversed_items = []
    for item in items:
        reversed_items.insert(0, item)
    return reversed_items


def reverse_list_builtin(items):
    """Reverse a list using Python's built-in slicing."""
    return items[::-1]


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print("Original:", data)
    print("Manually reversed:", reverse_list_manual(data))
    print("Built-in reversed:", reverse_list_builtin(data))
