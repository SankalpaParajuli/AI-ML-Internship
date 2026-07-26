"""
Exercise 10: Loop Patterns
Practice: for loops, while loops, break, continue, nested loops
"""

# for loop with range
print("Numbers 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print()

# while loop
print("\nCountdown:")
count = 5
while count > 0:
    print(count, end=" ")
    count -= 1
print("Liftoff!")

# break and continue
print("\nSkip 3, stop at 8:")
for i in range(1, 10):
    if i == 3:
        continue
    if i == 8:
        break
    print(i, end=" ")
print()

# nested loop - simple pattern
print("\nStar pattern:")
for row in range(1, 5):
    print("*" * row)
