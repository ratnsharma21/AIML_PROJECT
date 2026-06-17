# Project 1: Grade Calculator Based on Marks

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    try:
        marks_input = float(input("Enter Marks: "))
        if marks_input < 0 or marks_input > 100:
            print("Error: Marks must be between 0 and 100.")
        else:
            grade = calculate_grade(marks_input)
            print(f"Grade: {grade}")
    except ValueError:
        print("Invalid input! Please enter a valid number for marks.")
