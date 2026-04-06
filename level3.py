def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """
    Return the quotient of two numbers.
    
    Raises:
        ValueError: If the divisor is zero.
    """
    if b == 0.0:
        raise ValueError("Division by zero is not permitted.")
    return a / b

def main() -> None:
    """Execute the command-line calculator interface."""
    print("=== CLI Calculator ===")
    print("Supported operations: +, -, *, /")
    print("Input format: <number> <operator> <number>")
    print("Type 'exit' to terminate the application.\n")

    while True:
        try:
            user_input = input("Enter expression (or 'exit'): ").strip()
            if user_input.lower() == "exit":
                print("Calculator terminated. Goodbye.")
                break

            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid format. Please use: <number> <operator> <number>\n")
                continue

            operand1_str, operator, operand2_str = parts
            operand1, operand2 = float(operand1_str), float(operand2_str)

            if operator == "+":
                result = add(operand1, operand2)
            elif operator == "-":
                result = subtract(operand1, operand2)
            elif operator == "*":
                result = multiply(operand1, operand2)
            elif operator == "/":
                result = divide(operand1, operand2)
            else:
                print(f"Unsupported operator: '{operator}'.\n")
                continue

            print(f"Result: {result}\n")

        except ValueError as e:
            print(f"Error: {e}\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")


if name == "main":
    main()
