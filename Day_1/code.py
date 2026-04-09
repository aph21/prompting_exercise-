# ─────────────────────────────────────────────
# Find the Largest Number (without using max())
# ─────────────────────────────────────────────

def get_largest(numbers: list[int]) -> int:
    """Return the largest integer in a list using manual comparison."""
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest


def main():
    # 1. Get input from user
    try:
        raw = input("Enter integers separated by commas (e.g. 3, 7, 1, 9): ").strip()
    except EOFError:
        print("Error: No input provided. Please enter at least one integer.")
        return

    # 2. Validate: empty input
    if not raw:
        print("Error: No input provided. Please enter at least one integer.")
        return

    # 3. Parse and convert each value to int
    parts = raw.split(",")
    numbers = []
    for part in parts:
        try:
            numbers.append(int(part.strip()))
        except ValueError:
            print(f"Error: '{part.strip()}' is not a valid integer. Please enter integers only.")
            return

    # 4. Find and display the largest number
    result = get_largest(numbers)
    print(f"The largest number is: {result}")


if __name__ == "__main__":
    main()
