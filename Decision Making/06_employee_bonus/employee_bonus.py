# Determine employee bonus eligibility (Nested If)

def calculate_bonus(salary, years, rating):
    if years >= 2:
        if rating >= 4:
            bonus = salary * 0.20
            return f"Eligible for High Bonus! Bonus Amount: {bonus:.2f} (20% of salary)"
        elif rating == 3:
            bonus = salary * 0.10
            return f"Eligible for Standard Bonus! Bonus Amount: {bonus:.2f} (10% of salary)"
        else:
            return "No Bonus! Performance rating needs improvement."
    else:
        if rating == 5:
            bonus = salary * 0.05
            return f"Eligible for Starter Bonus! Bonus Amount: {bonus:.2f} (5% of salary)"
        else:
            return "No Bonus! Requires at least 2 years of service or outstanding performance."

if __name__ == "__main__":
    print("--- Employee Bonus Eligibility Calculator ---")
    try:
        emp_salary = float(input("Enter employee salary: "))
        emp_years = float(input("Enter years of service: "))
        emp_rating = int(input("Enter performance rating (1-5): "))
        
        if emp_salary < 0 or emp_years < 0 or emp_rating < 1 or emp_rating > 5:
            print("Invalid inputs! Please check salary, years, and rating ranges.")
        else:
            result = calculate_bonus(emp_salary, emp_years, emp_rating)
            print(result)
    except ValueError:
        print("Invalid input! Please enter appropriate numeric values.")
