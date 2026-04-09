import os

def get_student_name():
    """Continuously prompt for a valid student name (non-empty alphabetic string)."""
    while True:
        try:
            name = input("Enter student name: ").strip()
        except EOFError:
            print("Error: Name cannot be empty or invalid. Please try again.")
            continue
        
        # We allow spaces in names but check if characters are alphabetic
        if name and name.replace(" ", "").isalpha():
            return name
        else:
            print("Error: Name must be a non-empty alphabetic string. Please try again.")

def get_marks():
    """Continuously prompt for exactly 5 valid subject marks."""
    while True:
        try:
            raw_input = input("Enter marks for 5 subjects separated by commas (e.g. 80,90,70,60,50): ").strip()
        except EOFError:
            print("Error: Invalid input. Please try again.")
            continue
            
        parts = raw_input.split(",")
        
        if len(parts) != 5:
            print(f"Error: Expected exactly 5 marks, but got {len(parts)}. Please try again.")
            continue
            
        valid = True
        marks = []
        for part in parts:
            part = part.strip()
            try:
                mark = int(part)
                if 0 <= mark <= 100:
                    marks.append(mark)
                else:
                    print(f"Error: Mark '{mark}' is out of range. Must be between 0 and 100 inclusive.")
                    valid = False
                    break
            except ValueError:
                print(f"Error: '{part}' is not a valid integer.")
                valid = False
                break
                
        if valid:
            return marks
        else:
            print("Please re-enter the entire marks line.")

def calculate_grade_and_result(average):
    """Determine grade and pass/fail status based on average."""
    if average >= 81:
        return 'A', 'Pass'
    elif 66 <= average <= 80:
        return 'B', 'Pass'
    elif 51 <= average <= 65:
        return 'C', 'Pass'
    elif 35 <= average <= 50:
        return 'D', 'Pass'
    else:  # < 35
        return 'F', 'Fail'

def main():
    name = get_student_name()
    marks = get_marks()
    
    # Calculate average
    average = round(sum(marks) / 5)
    
    # Determine grade and result
    grade, result_status = calculate_grade_and_result(average)
    
    # Text output string
    marks_str_comma = ", ".join(str(m) for m in marks)
    
    # Console output
    print(f"Student: {name} | Average: {average} | Grade: {grade} | Result: {result_status}")
    
    # File output
    file_content = (
        f"Student Name: {name}\n"
        f"Marks: {marks_str_comma}\n"
        f"Average: {average}\n"
        f"Grade: {grade}\n"
        f"Result: {result_status}\n"
    )
    
    filename = f"{name}.txt"
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(file_content)
    except IOError as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    main()
