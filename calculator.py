"""
Simple Calculator
Author: Prachi
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def main():
    print("==== SIMPLE CALCULATOR ====")
    print("Operations: +  -  *  /")

    while True:
        num1 = float(input("\nEnter first number: "))
        op = input("Enter operation (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))

        if op == "+":
            result = add(num1, num2)
        elif op == "-":
            result = subtract(num1, num2)
        elif op == "*":
            result = multiply(num1, num2)
        elif op == "/":
            result = divide(num1, num2)
        else:
            print("Invalid operation.")
            continue

        print(f"Result: {result}")

        again = input("\nCalculate again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
