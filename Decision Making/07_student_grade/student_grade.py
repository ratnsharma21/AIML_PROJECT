# Student grade classification (elif Statements)

def classify_grade(marks):
    if marks >= 90:
        return "Grade A+"
    elif marks >= 80:
        return "Grade A"
    elif marks >= 70:
        return "Grade B"
    elif marks >= 60:
        return "Grade C"
    elif marks >= 50:
        return "Grade D"
    else:
        return "Grade F (Fail)"

if __name__ == "__main__":
    print("--- Student Grade Classifier ---")
    try:
        marks = float(input("Enter student marks (0-100): "))
        if marks < 0 or marks > 100:
            print("Error: Marks must be between 0 and 100.")
        else:
            grade = classify_grade(marks)
            print(f"For marks {marks}, the classification is: {grade}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
