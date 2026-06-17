# Check eligibility for college admission based on marks and age (Nested If)

def check_admission_eligibility(age, marks):
    if age >= 17:
        if marks >= 60:
            return "Eligible for admission! Both age and marks criteria met."
        else:
            return "Not Eligible! Marks must be at least 60%."
    else:
        return "Not Eligible! Minimum age required is 17."

if __name__ == "__main__":
    print("--- College Admission Eligibility Checker ---")
    try:
        age_input = int(input("Enter your age: "))
        marks_input = float(input("Enter your marks percentage (0-100): "))
        
        if age_input < 0 or marks_input < 0 or marks_input > 100:
            print("Invalid inputs! Please enter realistic values.")
        else:
            result = check_admission_eligibility(age_input, marks_input)
            print(result)
    except ValueError:
        print("Invalid input format! Please enter numbers only.")
