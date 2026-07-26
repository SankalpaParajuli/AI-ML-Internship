"""
Calculator (CLI)
-----------------
A simple command-line calculator that supports +, -, *, /, and ** (power).
Demonstrates: functions, loops, conditionals, exception handling, input().
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def power(a, b):
    return a ** b


OPERATIONS = {
    "1": ("Add (+)", add),
    "2": ("Subtract (-)", subtract),
    "3": ("Multiply (*)", multiply),
    "4": ("Divide (/)", divide),
    "5": ("Power (**)", power),
}


def show_menu():
    print("\n===== Simple Calculator =====")
    for key, (label, _) in OPERATIONS.items():
        print(f"  {key}. {label}")
    print("  6. Exit")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number, please try again.")


def main():
    print("Welcome to the Week 1 CLI Calculator!")
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "6":
            print("Goodbye!")
            break

        if choice not in OPERATIONS:
            print("Invalid choice, please select 1-6.")
            continue

        label, operation = OPERATIONS[choice]
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            result = operation(num1, num2)
            print(f"Result: {num1} {label.split('(')[1][:-1]} {num2} = {result}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
