# Check whether a person is eligible to vote

def check_voting_eligibility(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return f"Not eligible to vote. You need to wait {18 - age} more year(s)."

if __name__ == "__main__":
    print("--- Voting Eligibility Checker ---")
    try:
        age_input = int(input("Enter your age: "))
        if age_input < 0:
            print("Age cannot be negative!")
        else:
            result = check_voting_eligibility(age_input)
            print(result)
    except ValueError:
        print("Invalid input! Please enter a valid integer for age.")
