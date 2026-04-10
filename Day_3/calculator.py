def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Bug: crashes when b is 0
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        if op == '+':
            print(f"Result: {add(num1, num2)}")
        elif op == '-':
            print(f"Result: {subtract(num1, num2)}")
        elif op == '*':
            print(f"Result: {multiply(num1, num2)}")
        elif op == '/':
            # Calling divide, still intentionally missing zero-division handling inside divide()
            print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid operator.")
    except ValueError:
        print("Please enter valid numbers.")
