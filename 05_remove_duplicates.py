"""
Exercise 05: Remove Duplicates from a List
Practice: sets, loops, preserving order
"""


def remove_duplicates_preserve_order(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


if __name__ == "__main__":
    data = [1, 2, 2, 3, 4, 4, 4, 5, 1]
    print("Original:", data)
    print("Using set (order not guaranteed):", list(set(data)))
    print("Preserving order:", remove_duplicates_preserve_order(data))
