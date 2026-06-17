# EMI (Equated Monthly Installment) Calculator Function

def calculate_emi(principal, annual_rate, tenure_months):
    r = annual_rate / (12 * 100)
    n = tenure_months
    
    if r == 0:
        return principal / n
        
    emi = principal * r * ((1 + r) ** n) / (((1 + r) ** n) - 1)
    return emi

if __name__ == "__main__":
    print("--- Loan EMI Calculator ---")
    try:
        p = float(input("Enter loan principal amount: "))
        rate = float(input("Enter annual interest rate (e.g. 10.5 for 10.5%): "))
        years = float(input("Enter tenure in years: "))
        
        months = int(years * 12)
        
        if p <= 0 or rate < 0 or months <= 0:
            print("Error: Input values must be positive.")
        else:
            emi_amount = calculate_emi(p, rate, months)
            total_payment = emi_amount * months
            total_interest = total_payment - p
            
            print(f"\nMonthly EMI: {emi_amount:.2f}")
            print(f"Total Amount Payable: {total_payment:.2f}")
            print(f"Total Interest Payable: {total_interest:.2f}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")
