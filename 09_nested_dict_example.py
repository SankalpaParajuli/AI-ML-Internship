"""
Exercise 09: Nested Dictionaries
Practice: accessing and looping through nested data structures
"""

students = {
    "S001": {"name": "Sankalpa", "marks": {"python": 85, "ml": 78}},
    "S002": {"name": "Alina", "marks": {"python": 90, "ml": 88}},
    "S003": {"name": "Bibek", "marks": {"python": 70, "ml": 65}},
}

print("All students:\n")
for student_id, info in students.items():
    print(f"ID: {student_id}")
    print(f"  Name: {info['name']}")
    for subject, mark in info["marks"].items():
        print(f"  {subject}: {mark}")
    average = sum(info["marks"].values()) / len(info["marks"])
    print(f"  Average: {average:.2f}\n")
