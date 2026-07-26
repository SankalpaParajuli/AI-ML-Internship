"""
Exercise 17: File Write and Read
Practice: basic file I/O using 'with open(...)'
"""

FILENAME = "sample_output.txt"

lines_to_write = [
    "Week 1 - Python & Environment Setup\n",
    "Learning core Python and Git/GitHub workflow.\n",
    "Building a strong base before ML modelling starts.\n",
]

# Writing to a file
with open(FILENAME, "w", encoding="utf-8") as f:
    f.writelines(lines_to_write)
print(f"Wrote {len(lines_to_write)} lines to {FILENAME}")

# Reading the whole file
with open(FILENAME, "r", encoding="utf-8") as f:
    content = f.read()
print("\nFull file content:")
print(content)

# Reading line by line
with open(FILENAME, "r", encoding="utf-8") as f:
    print("Line by line:")
    for i, line in enumerate(f, start=1):
        print(f"  Line {i}: {line.strip()}")

# Appending to a file
with open(FILENAME, "a", encoding="utf-8") as f:
    f.write("This line was appended.\n")

print("\nAfter appending, file content:")
with open(FILENAME, "r", encoding="utf-8") as f:
    print(f.read())
