# Scholarship eligibility checker using logical operators

def check_scholarship(gpa, annual_income, is_sports_champion):
    
    if gpa >= 3.5 and (annual_income < 250000 or is_sports_champion):
        return "Eligible for Scholarship! Criteria met successfully."
    else:
        reasons = []
        if gpa < 3.5:
            reasons.append("GPA must be at least 3.5 (current GPA is too low).")
        if annual_income >= 250000 and not is_sports_champion:
            reasons.append("Annual income must be below 250,000 unless you are a sports champion.")
            
        return "Not Eligible for Scholarship. Reasons:\n- " + "\n- ".join(reasons)

if __name__ == "__main__":
    print("--- Scholarship Eligibility Checker ---")
    try:
        candidate_gpa = float(input("Enter GPA (0.0 to 4.0): "))
        income = float(input("Enter annual family income: "))
        sports_input = input("Are you a state/national level sports champion? (yes/no): ").strip().lower()
        
        is_sports = sports_input in ["yes", "y", "true"]
        
        if candidate_gpa < 0.0 or candidate_gpa > 4.0 or income < 0:
            print("Error: GPA must be between 0.0 and 4.0 and income must be positive.")
        else:
            status = check_scholarship(candidate_gpa, income, is_sports)
            print(status)
    except ValueError:
        print("Invalid input format! Please enter valid numeric values.")
