#PROMPT 1:
# Task: write a python script, which should be able to take a list of numbers from user and then should return the largest number from that list
# before writing script, plan the implementation, only when you are fully confident about your plan and script then implement the script and verify the result

# ─── PLAN ────────────────────────────────────────────────────────────────────
# 1. Prompt the user to enter numbers separated by spaces.
# 2. Split the input string into individual tokens.
# 3. Convert each token to a float (supports integers & decimals).
# 4. Validate: ensure the list is non-empty and all values are numeric.
# 5. Use Python's built-in max() to find the largest number.
# 6. Display the result.
# ─────────────────────────────────────────────────────────────────────────────


def get_largest_number():
    """Takes a list of numbers from the user and returns the largest one."""

    user_input = input("Enter numbers separated by spaces: ").strip()

    # Guard: empty input
    if not user_input:
        print("Error: No numbers were entered. Please provide at least one number.")
        return

    tokens = user_input.split()

    # Convert tokens to floats, catching any non-numeric values
    numbers = []
    for token in tokens:
        try:
            numbers.append(float(token))
        except ValueError:
            print(f"Error: '{token}' is not a valid number. Please enter numeric values only.")
            return

    largest = max(numbers)

    # Display as int if the value is a whole number, else as float
    display = int(largest) if largest == int(largest) else largest
    print(f"\nNumbers entered : {[int(n) if n == int(n) else n for n in numbers]}")
    print(f"Largest number  : {display}")


if __name__ == "__main__":
    get_largest_number()
