"""
Exercise 08: Merge Dictionaries
Practice: dictionary merging, update(), unpacking
"""

defaults = {"theme": "light", "font_size": 12, "language": "en"}
user_prefs = {"font_size": 16, "language": "ne"}

# Method 1: using update()
merged_v1 = defaults.copy()
merged_v1.update(user_prefs)
print("Merged using update():", merged_v1)

# Method 2: using dictionary unpacking (Python 3.5+)
merged_v2 = {**defaults, **user_prefs}
print("Merged using unpacking:", merged_v2)

# Method 3: using | operator (Python 3.9+)
merged_v3 = defaults | user_prefs
print("Merged using | operator:", merged_v3)
