"""
Exercise 19: Simple CSV-like Parser (without using the csv module)
Practice: file I/O, string split, list of dicts - good warm up before pandas
"""

FILENAME = "students.csv"


def create_sample_csv(filename):
    data = (
        "name,age,course\n"
        "Sankalpa,20,Computing\n"
        "Alina,21,Computing\n"
        "Bibek,22,IT\n"
    )
    with open(filename, "w", encoding="utf-8") as f:
        f.write(data)


def parse_csv(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    header = lines[0].split(",")
    records = []
    for line in lines[1:]:
        values = line.split(",")
        record = dict(zip(header, values))
        records.append(record)
    return records


if __name__ == "__main__":
    create_sample_csv(FILENAME)
    students = parse_csv(FILENAME)

    print("Parsed records:")
    for student in students:
        print(f"  {student}")

    print("\nJust the names:")
    names = [s["name"] for s in students]
    print(names)
