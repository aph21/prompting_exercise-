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
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 2 = {subtract(10, 2)}")
    print(f"4 * 6 = {multiply(4, 6)}")
    
    # The following line will crash the program instead of handling the error gracefully:
    print(f"8 / 0 = {divide(8, 0)}")
