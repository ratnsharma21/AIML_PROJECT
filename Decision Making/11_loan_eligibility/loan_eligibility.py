# Loan eligibility checker using logical operators

def check_loan_eligibility(age, income, credit_score, has_defaults):
    
    if (age >= 21 and age <= 60) and income >= 30000 and credit_score >= 700 and not has_defaults:
        return "Congratulations! You are ELIGIBLE for the loan."
    else:
        reasons = []
        if not (age >= 21 and age <= 60):
            reasons.append("Age must be between 21 and 60 years.")
        if income < 30000:
            reasons.append("Monthly income must be at least 30,000.")
        if credit_score < 700:
            reasons.append("Credit score must be at least 700.")
        if has_defaults:
            reasons.append("Cannot have active unpaid loan defaults.")
        
        return "Not Eligible for the loan. Reasons:\n- " + "\n- ".join(reasons)

if __name__ == "__main__":
    print("--- Loan Eligibility Checker ---")
    try:
        user_age = int(input("Enter your age: "))
        user_income = float(input("Enter monthly income: "))
        user_credit = int(input("Enter credit score (300-850): "))
        defaults_input = input("Do you have any active unpaid defaults? (yes/no): ").strip().lower()
        
        has_defaults = defaults_input == "yes" or defaults_input == "y"
        
        if user_age < 0 or user_income < 0 or user_credit < 300 or user_credit > 850:
            print("Error: Please enter valid positive values within normal ranges.")
        else:
            status = check_loan_eligibility(user_age, user_income, user_credit, has_defaults)
            print(status)
    except ValueError:
        print("Invalid input format! Please enter valid numbers.")
