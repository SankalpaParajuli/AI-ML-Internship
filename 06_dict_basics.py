"""
Exercise 06: Dictionary Basics
Practice: creating, accessing, updating, looping through dictionaries
"""

student = {
    "name": "Sankalpa",
    "age": 20,
    "course": "BSc (Hons) Computing",
    "skills": ["Python", "Java", "SQL"]
}

print("Student dict:", student)
print("Name:", student["name"])
print("Skills:", student.get("skills"))

# Add / update a key
student["internship"] = "Code-IT"
student["age"] = 21
print("After update:", student)

# Loop through keys and values
print("\nAll key-value pairs:")
for key, value in student.items():
    print(f"  {key}: {value}")

# Check existence
if "course" in student:
    print("\n'course' key exists in student dict")

# Remove a key
del student["age"]
print("\nAfter deleting 'age':", student)
